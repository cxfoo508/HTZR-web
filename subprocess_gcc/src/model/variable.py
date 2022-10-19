class DefVar():
    name:str = ""
    type_:str = ""
    hasVal:bool = False
    val:str = ""

    def __init__(self, name, type_, hasVal=False, val=''):
        self.name = name
        self.type_ = type_
        self.hasVal = hasVal
        self.val = val

    def getAssign(self):
        return "{} = {};".format(self.name, self.val)

    def getDeclare(self):
        declareLine = "{} {}".format(self.type_, self.name)
        assignLines = []
        if self.hasVal:
            if type(self.val) == list:
                declareLine += ";"
                for val in self.val:
                    if type(val.val) != list:
                        assignLines.append("\n\t{}.{}".format(self.name, val.getAssign()))
                    else:
                        assignLines.append("\n\t")
                        assignLines.append(val.getDeclare())
                        assignLines.append("\n\t{}.{} = {};".format(self.name, val.name, val.name))
            else:
                declareLine += " = {};".format(self.val)
        else:
            declareLine += ";"

        return declareLine + "".join(assignLine for assignLine in assignLines)
