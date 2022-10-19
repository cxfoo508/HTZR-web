class DefFunc():
    name:str = ""
    type_:str= ""
    params = [] 
    rtn:str = ""
    description:str = ""

    def __init__(self, name, type_="", params=[], rtn="", description=""):
        self.name = name
        self.type_ = type_ if type_!=None else ""
        self.params = params if params!=None else []
        self.rtn = str(rtn) if rtn!=None else ""
        self.description = description if description!=None else ""

    def getDeclare(self):
        return "{} {} ({})".format(self.type_, self.name, "" if len(self.params)<=0 else ", ".join(param[list(param.keys())[0]]+" "+list(param.keys())[0] for param in self.params))

    def getRtn(self):
        return "" if len(self.rtn)==0 else (" "+str(self.rtn))