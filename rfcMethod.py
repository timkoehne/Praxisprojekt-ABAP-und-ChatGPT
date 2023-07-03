import importlib
import json
import pyrfc
import ast
import os
import typing

from chatGptWrapper import ChatGPT

    
numRepeats = 1
chatgpt = ChatGPT(systemMessage="always generate a abap function module including the interface comment. no explanations or examples.")

class Test:
    def __init__(self, functionName, importParameters, exportParameters) -> None:
        self.functionName = functionName
        self.importParameters = importParameters
        self.exportParameters = exportParameters
    
    def callFunction(self, *args):
        
        # todo checkParameterCompatibility
        #input and export
        #check type matches python type
        
        #i - int
        #f - float
        #p - Decimal
        #c - unicode str
        #d - datetime.date or string
        #t - datetime.time or string
        #n - str[bytes]
        #string - unicode str
        #xstring - str[bytes]
        #struct - {}
        #itab - [{}, {}]
        
        callParams = buildParameters(args, self.importParameters)
        print("Functioncall with Parameters: " + str(callParams))
        result = callFunctionModule(self.functionName, callParams)
        print("Result: " + str(result))
        result = result[list(result)[0]]
        return result

class AbapVariable:
    def __init__(self, abapCodeLine: str) -> None:
        self.varName = abapCodeLine.split(" ")[0].replace("VALUE(", "").replace(")", "").upper().removesuffix(".")

        self.varType = " ".join(" ".join(abapCodeLine.split()).split()[2:]).upper().removesuffix(".")
        # if self.varType == "STANDARD TABLE OF STRING":
        #     self.varType = "stringtab"

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

def createFunctionModule(functionName, programcode, importParameters, exportParameters):
    programcode = [line for line in programcode if not line.startswith("*\"")]
    programcode = programcode[1:] if programcode[0].startswith("FUNCTION") else programcode
    programcode = programcode[:-1] if programcode[-1].startswith("ENDFUNCTION.") else programcode
    
    try: 
        print("Creating function module " + functionName)
        result = conn.call('RS_FUNCTIONMODULE_INSERT',
                        FUNCNAME=functionName,
                        FUNCTION_POOL="ZRFCTEST",
                        SHORT_TEXT="",
                        REMOTE_CALL="X",
                        SOURCE=programcode,
                        IMPORT_PARAMETER=importParameters,
                        EXPORT_PARAMETER=exportParameters)
        return True
        print("successfully created function module")
    except pyrfc._exception.ABAPApplicationError as e:
        print("FunctionCreate: ApplicationError " + str(e))
    except pyrfc._exception.ABAPRuntimeError as e:
        print("FunctionCreate: RuntimeError " + str(e.key))
    except pyrfc._exception.LogonError as e:
        print("FunctionCreate: LogonError " + str(e.key))
    except pyrfc._exception.CommunicationError as e:
        print("FunctionCreate: CommunicationError " + str(e.key))
    except Exception as e:
        print("FunctionCreate: " + str(e))
        print(e)
    return False

def callFunctionModule(functionName, callParams) -> dict:
    try:
        result = conn.call(functionName, **callParams)
        return result
    except pyrfc._exception.ABAPApplicationError as e:
        result = "FunctionCall: ApplicationError " + str(e.key)
    except pyrfc._exception.ABAPRuntimeError as e:
        result = "FunctionCall: RuntimeError " + str(e)
    except pyrfc._exception.LogonError as e:
        result = "FunctionCall: LogonError " + str(e.key)
    except pyrfc._exception.CommunicationError as e:
        result = "FunctionCall: CommunicationError " + str(e.key)
    except TypeError as e:
        result = "FunctionCall: TypeError: " + str(callParams)
    except Exception as e:
        result = repr(e)
    return {"exception": result}

def deleteFunctionModule(functionName):
    conn.call("Z_FUNCTION_DELETE", FUNCNAME=functionName)

def buildParameters(params, importParameters):    
    callParams = {}
    for index, parameter in enumerate(importParameters):
        callParams[parameter["PARAMETER"]] = params[index]
    return callParams

def getPrompt(promptNumber):
    with open("only prompts/" + str(promptNumber) + ".txt") as file:
        prompt = file.read()
        print("Prompt " + str(promptNumber) + ":")
        print(prompt)
        return prompt

def extractInformation(programcde):
    functionName = programcode[0].split()[-1].upper().removesuffix(".")
    importParameters, exportParameters = parseInterface(programcode)
        
    print("Functionname: " + functionName)
    for entry in importParameters:
        print("Import: " + str(entry))
    for entry in exportParameters:
        print("Export: " + str(entry))
    return functionName, importParameters, exportParameters

def checkParameterCompatibility(params, importParameters, exportParameters):
    try:
        if len(params) != len(importParameters):
            raise IndexError
        
        #todo input types
        #todo export types
        
        return True
    except IndexError:
        print("Wrong number of parameters. Function expects {0} but provided were {1}".format(len(importParameters), len(params)))
    return False

with open("saplogonLoginDetails - local.json", "r") as file:
    connection_params = json.loads(file.read())

with pyrfc.Connection(**connection_params) as conn:
    # allPrompts = range(0, 164)
    for promptNumber in [23]:
        prompt = getPrompt(promptNumber)
            
        for i in range(0, numRepeats):
            programcode = chatgpt.askWithoutContext(prompt).split("\n")
            print("ChatGPT Answer: ")
            for line in programcode:
                print(line)
            
            functionName, importParameters, exportParameters = extractInformation(programcode)
            
            functionCreated = createFunctionModule(functionName, programcode, importParameters, exportParameters)
            
            #todo parameter type checks in test.callfunction
            
            testModule = importlib.import_module("adjustedTests.test" + str(promptNumber))
            passed, failed = testModule.check(Test(functionName, importParameters, exportParameters).callFunction)
            print("Passed: " + str(passed) +" out of " + str(passed+failed))
            
            deleteFunctionModule(functionName)