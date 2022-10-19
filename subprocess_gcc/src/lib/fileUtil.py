def FileWrite(filepath:str, outStr:str):
    fileOut = open(filepath, "w", encoding="utf-8")
    fileOut.write(outStr)
    fileOut.close()

def FileReads(filepath:str):
    fileOut = open(filepath, "r", encoding="utf-8")
    lines = fileOut.readlines()
    fileOut.close()
    return lines

def FileRead(filepath:str):
    fileOut = open(filepath, "r", encoding="utf-8")
    string = fileOut.read()
    fileOut.close()
    return string