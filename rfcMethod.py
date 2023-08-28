
import json
import more_itertools
import threading
import queue
import pythonAbapInterface

class Test:
    def __init__(self, conn, functionName, importParameters, exportParameters, saveTo) -> None:
        self.conn = conn
        self.functionName = functionName
        self.importParameters = importParameters
        self.exportParameters = exportParameters
        self.saveTo = saveTo
        self.saveTo["functionCalls"] = []
    
    def callFunction(self, *args):
        callParams = buildAbapImportParameters(args, self.importParameters)
        result = pythonAbapInterface.callFunctionModule(self.conn, self.functionName, callParams)
        
        self.saveTo["functionCalls"].append(result)
        if len(result) > 0:
            result = result[list(result)[0]]
        return result

class AbapVariable:
    def __init__(self, abapCodeLine: str) -> None:
        self.varName = abapCodeLine.split(" ")[0].replace("VALUE(", "").replace(")", "").upper().removesuffix(".")
        self.varType = " ".join(" ".join(abapCodeLine.split()).split()[2:]).upper().removesuffix(".")

def parseAbapFunctionInterface(chatgptResponse: list[str]):
    interface = [line for line in chatgptResponse if line.startswith("*")]
    interface = [line.replace("*\"", "").strip() for line in interface]
    interface = [line for line in interface if line.strip("-")]
    imports = []
    exports = []
    state = None
    for line in interface:
        if(line == "IMPORTING" or line == "EXPORTING"):
            state = line
            continue
        if state == "IMPORTING":
            imports.append(line)
        elif state == "EXPORTING":
            exports.append(line)
        
    importVariables = [AbapVariable(line) for line in imports]
    exportVariables = [AbapVariable(line) for line in exports]
        
    importParameters = [{"PARAMETER": parameter.varName, "TYP": parameter.varType} for parameter in importVariables]
    exportParameters = [{"PARAMETER": parameter.varName, "TYP": parameter.varType} for parameter in exportVariables]
    
    return importParameters, exportParameters

def buildAbapImportParameters(params, importParameters):    
    callParams = {}
    
    smaller = len(params) if len(params) <= len(importParameters) else len(importParameters)
    for index in range(0, smaller):
        key = list(importParameters)[index]
        callParams[key["PARAMETER"]] = params[index]

    return callParams

def getPrompt(folderPath: str, promptNumber: int):
    with open(folderPath + str(promptNumber) + ".txt") as file:
        prompt = file.read()
        return prompt

def extractAbapFunctionInformation(chatgptResponse: list[str]):
    functionName = chatgptResponse[0].split()[1].upper().removesuffix(".")
    importParameters, exportParameters = parseAbapFunctionInterface(chatgptResponse)
    
    programcode = [line for line in chatgptResponse if not line.startswith("*")]
    programcode = programcode[1:] if programcode[0].startswith("FUNCTION") else programcode
    programcode = programcode[:-1] if programcode[-1].startswith("ENDFUNCTION.") else programcode
    
    return functionName, importParameters, exportParameters, programcode