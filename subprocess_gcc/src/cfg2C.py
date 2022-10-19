import yaml
import json
import os 
import shutil
from jinja2 import Environment, FileSystemLoader
from model.func import DefFunc
from model.variable import DefVar
from model.flow import DefFlow, FlowResult, FlowParam, FlowCheck
from model.case import TCase
from lib.zip import make_zip
from testRunner import CompileProject, RunProject

def json2Yaml(jsonObj):
    json_str = json.dumps(jsonObj) #{"a":"b","c":4})
    return yaml.load(json_str, Loader = yaml.Loader)

def yaml2Str(yamlObj, default_flow_style=False):
    # if default_flow_style == True, will print json, else print yaml
    return yaml.dump(yamlObj, default_flow_style=default_flow_style, Dumper = yaml.Dumper)

def readYamlFromFile(fileName:str="2.yml"):
    file0 = open("rsc/configs_repo/"+fileName,"r", encoding="utf-8")
    # May cause exception! But should corrupt!
    document = file0.read()
    yamlObj = yaml.load(document, Loader = yaml.Loader)
    #print(yaml.dump(yamlObj, default_flow_style=False, Dumper = yaml.Dumper))
    file0.close()
    return yamlObj

def recurDefValDecode(declare):
    name = list(declare.keys())[0]
    attr = declare[list(declare.keys())[0]]
    defVar = DefVar(name=name, type_=attr["type"])
    if type(attr["val"])==list:
        defVar.val = []
        for declareInner in attr["val"]:
            defVar.val.append(recurDefValDecode(declareInner))
    else:
        defVar.val = None if type(attr["val"])==type(None) else attr["val"]
    defVar.hasVal = False if defVar.val == None else True
    return defVar

def yaml2TCase(yamlObj):
    tCaseList = []
    for key, content in yamlObj.items():
        tCase = TCase()
        tCase.id = content["id"]
        tCase.name = content["name"]
        tCase.description = content["description"]
        tCase.flowInfo = content["flowInfo"]
        tCase.people = content["people"]
        tCase.headers = content["headerFiles"]
        for func in content["defFuncList"]:
            funcName = list(func.keys())[0]
            funcAttr = func[list(func.keys())[0]]
            defFunc = DefFunc(name=funcName, type_=funcAttr["type"], params=funcAttr["params"], rtn=funcAttr["return"], description=funcAttr["description"])
            tCase.defFuncs.append(defFunc)
            
        # recursively decode variable declaration
        for declare in content["declareList"]:
            tCase.declareVarList.append(recurDefValDecode(declare))

        for flow in content["flows"]:
            flowName = list(flow.keys())[0]
            attr = flow[list(flow.keys())[0]]
            params = []
            for param in attr["paramList"]:
                pName = list(param.keys())[0]
                attr_param = param[list(param.keys())[0]]
                params.append(FlowParam(name=str(attr_param["name"]), cfg=attr_param["cfg"], type_=attr_param["type"]))
            checks = []
            for check in attr["checks"]:
                cName = list(check.keys())[0]
                attr_check = check[list(check.keys())[0]]
                if type(attr_check) != dict:
                    checks.append(FlowCheck(name=cName, targetVal=attr_check, op_="=="))
                else:
                    checks.append(FlowCheck(name=cName, targetVal=attr_check["val"], op_=attr_check["op"]))

            flowFunc = DefFlow(
                name=flowName, 
                description=attr["description"] if "description" in attr.keys() else "", 
                params = params, 
                result = FlowResult(name=attr["result"]["name"], isNew=(attr["result"]["isNew"]=="y" or attr["result"]["isNew"]=="Y"), type_=attr["result"]["type"]),
                checks = checks,
            )
            tCase.defFlows.append(flowFunc)

        if "clearFlowList" in content.keys():
            for flow in content["clearFlowList"]:
                flowName = list(flow.keys())[0]
                attr = flow[list(flow.keys())[0]]
                params = []
                for param in attr["paramList"]:
                    pName = list(param.keys())[0]
                    attr_param = param[list(param.keys())[0]]
                    params.append(FlowParam(name=attr_param["name"], cfg=attr_param["cfg"], type_=attr_param["type"]))
            
                tCase.clearFlows.append(
                    DefFlow(
                        name=flowName, 
                        description=attr["description"] if "description" in attr.keys() else "", 
                        params = params,
                        result=None, 
                    )
                )

        #print(tCase.id, tCase.defFuncs)
        tCaseList.append(tCase)
    return tCaseList

def mockTCase():
    tCase = TCase()
    tCase.id = 1
    tCase.name = "test_pthread_create"
    tCase.description = "测试1"
    tCase.flowInfo = "测试1111"
    tCase.declareVarList = [
        DefVar(name="pthread_id", type_="int*"),
        DefVar(name="some_str", type_="const char*", hasVal=True, val='"abc123"'),
    ]
    tCase.headers = ["2.h","3.h"]
    tCase.defFuncs = [
        DefFunc(name="func1", type_="void*", params=[{"id":"int*"}], rtn="NULL", description="这是一个线程函数"),
        DefFunc(name="func2", type_="void*", params=[{"id":"int*"}], rtn="NULL", description="这是一个线程函数"),
    ]
    tCase.defFlows = [
        DefFlow(name="pthread_create", description="创建线程", 
            params=[FlowParam(name="pthread_id"), FlowParam(name="0")],
            result=FlowResult(name="status0", isNew=True, type_="int"), 
            checks=[FlowCheck(name="status0",targetVal="0"), FlowCheck(name="pthread_id",targetVal="-1", op_="!=")],
        ),
        DefFlow(name="pthread_join", description="等待线程", 
            params=[FlowParam(name="pthread_id"), FlowParam(name="0")],
            result=FlowResult(name="status0", isNew=False, type_="int"), 
            checks=[FlowCheck(name="status0",targetVal="0"), FlowCheck(name="pthread_id",targetVal="-1", op_="!=")],
        ),
    ]
    tCase.clearFlows = [
        DefFlow(name="pthread_join", description="等待线程", 
            params=[FlowParam(name="pthread_id")],
            result=None, 
        ),
    ]
    return tCase

def toCCase(tCase: TCase, outFileNamePrefix:str, printOutput=False, storeOutFile=True):
    file_loader = FileSystemLoader('rsc/templates')
    env = Environment(loader=file_loader)
    template = env.get_template('testcase.tpl.c')
    output = template.render(description=tCase.description,
                            id = tCase.id,
                            name = tCase.name,
                            flowInfo = tCase.flowInfo,
                            headersLen=len(tCase.headers),
                            headers=tCase.headers,
                            defFuncLen=len(tCase.defFuncs), 
                            defFuncs=tCase.defFuncs, 
                            defVarLen=len(tCase.declareVarList), 
                            defVars=tCase.declareVarList,
                            defFlowLen=len(tCase.defFlows), 
                            defFlows=tCase.defFlows,
                            clearFlowLen=len(tCase.clearFlows), 
                            clearFlows=tCase.clearFlows
                        )
    if printOutput:
        print(output)
    if storeOutFile:
        fileOut = open("{}".format(outFileNamePrefix),"w",encoding="utf-8")
        fileOut.write(output)
        fileOut.close()
    return output

def toCFrame(u_id:str, tCaseList):
    # gen maintest.c
    path0 = "out/"+u_id
    if os.path.exists(path0):
        #os.removedirs(path0)
        shutil.rmtree(path0)
    os.mkdir(path0)
    os.mkdir(path0+"/include")
    os.mkdir(path0+"/caseset")
    tCaseName = []
    for tCase in tCaseList:
        toCCase(tCase, path0+"/caseset/"+tCase.name+".c")
        tCaseName.append(tCase.name)
    file_loader = FileSystemLoader('rsc/templates')
    env = Environment(loader=file_loader)
    template = env.get_template('maintest.tpl.c')
    output = template.render(caseLen = len(tCaseName), tCases = tCaseName)
    fileOut = open("out/{}/maintest.c".format(u_id),"w",encoding="utf-8")
    fileOut.write(output)
    fileOut.close()
    shutil.copyfile("rsc/templates/basic.h", "out/{}/include/basic.h".format(u_id))
    shutil.copyfile("rsc/templates/makefile", "out/{}/makefile".format(u_id))
    CompileProject("out/{}".format(u_id))
    RunProject("out/{}".format(u_id))
    # make zip
    make_zip("out/{}".format(u_id), "out/{}.zip".format(u_id))


if __name__ == '__main__':
    # 1. mock TCase & genC
    #toCCase(mockTCase(), "out/testcase1.c")
    #for tCase in tCaseList:
    #    toCCase(tCase, "out/"+tCase.name+".c")

    # 2. read yaml & decode TCase & genC
    #tCaseList = yaml2TCase(readYamlFromFile())
    #toCFrame("ii88", tCaseList)

    # 3. read yaml & print string
    print(yaml2Str(readYamlFromFile("2.yml"), True))