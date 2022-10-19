class FlowResult():
    name:str = ""
    isNew:bool = False
    type_:str = ""

    # if isNew == True, type_ must be set!
    def __init__(self, name, isNew=False, type_=""):
        self.name = name
        self.isNew = isNew
        self.type_ = type_

    def getDeclare(self):
        return (self.type_+" " if self.isNew else "") + self.name + " = " 

class FlowParam():
    name:str = ""
    cfg:str = ""
    type_:str = ""

    # if cfg not None, type_ must be set!
    def __init__(self, name, cfg="", type_=""):
        self.name = name
        self.cfg = cfg
        self.type_ = type_

    # 暂时不支持cfg
    def getDeclare(self):
        return (self.name)

class FlowCheck():
    name:str = ""
    targetVal:str = "0"
    op_:str = ""

    # if cfg not None, type_ must be set!
    def __init__(self, name, targetVal="0", op_="=="):
        self.name = name
        self.targetVal = targetVal
        self.op_ = op_

    def getDeclare(self):
        return "if ({} {} {})".format(self.name, self.op_, self.targetVal)

class DefFlow():
    name:str = ""
    description:str = ""
    params = []
    result:FlowResult = None
    checks = []

    def __init__(self, name, description="", params=[], result=None, checks=[]):
        self.name = name
        self.description = description if description!=None else description
        self.params = params
        self.result = result
        self.checks = checks

    def getCheckLen(self):
        return len(self.checks)

    def getCall(self):
        return "{}({})".format(self.name, "" if len(self.params)<=0 else ", ".join(param.getDeclare() for param in self.params))