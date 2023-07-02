import json
import pyrfc
import ast
import os
import typing

class AbapVariable:
    def __init__(self, abapCodeLine: str) -> None:
        self.varName = abapCodeLine.split(" ")[0].replace("VALUE(", "").replace(")", "").upper().removesuffix(".")
        self.varType = abapCodeLine.split(" ")[2].upper().removesuffix(".")

def parseInterface(programcode):
    interface  = [line for line in programcode if line.startswith("*\"")]
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

with open("saplogonLoginDetails - local.json", "r") as file:
    connection_params = json.loads(file.read())


with pyrfc.Connection(**connection_params) as conn:
    
    with open("answer.txt", "r") as file:
        programcode = file.read().splitlines()
    
    #find function name and parameters
    functionName = programcode[0].split(" ")[1].upper().removesuffix(".")
    importParameters, exportParameters = parseInterface(programcode)
    for entry in importParameters:
        print("Import: " + str(entry))
    for entry in exportParameters:
        print("Export: " + str(entry))
     
    programcode = [line for line in programcode if not line.startswith("*\"")]
    programcode = programcode[1:] if programcode[0].startswith("FUNCTION") else programcode
    programcode = programcode[:-1] if programcode[-1].startswith("ENDFUNCTION.") else programcode
    # for line in programcode:
    #     print(line)
    
    
    #create function module 
    result = conn.call('RS_FUNCTIONMODULE_INSERT',
                       FUNCNAME=functionName,
                       FUNCTION_POOL="ZRFCTEST",
                       SHORT_TEXT="",
                       REMOTE_CALL="X",
                       SOURCE=programcode,
                       IMPORT_PARAMETER=importParameters,
                       EXPORT_PARAMETER=exportParameters)


    #call function module
    params = ["hello there"]
    callParams = {}
    for index, parameter in enumerate(importParameters):
        callParams[parameter["PARAMETER"]] = params[index]
    result = conn.call(functionName, **callParams)
    print(result)
    
    #delete function module
    conn.call("Z_FUNCTION_DELETE", FUNCNAME=functionName)
    
    #todo catch errors:
    #wrong number of parameters
    #wrong parameter types
    #
    
