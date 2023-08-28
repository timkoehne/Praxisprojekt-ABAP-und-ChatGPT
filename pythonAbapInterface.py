import pyrfc
def createFunctionModule(conn, functionName, importParameters, exportParameters, programcode):
    try: 
        result = conn.call('RS_FUNCTIONMODULE_INSERT',
                        FUNCNAME=functionName,
                        FUNCTION_POOL="ZRFCTEST",
                        SHORT_TEXT="",
                        REMOTE_CALL="X",
                        SOURCE=programcode,
                        IMPORT_PARAMETER=importParameters,
                        EXPORT_PARAMETER=exportParameters)
        return "success"
    except pyrfc._exception.ABAPApplicationError as e:
        return "FunctionCreate: ApplicationError " + str(e)
        pass
    except pyrfc._exception.ABAPRuntimeError as e:
        return "FunctionCreate: RuntimeError " + str(e.key)
        pass
    except pyrfc._exception.LogonError as e:
        return "FunctionCreate: LogonError " + str(e.key)
        pass
    except pyrfc._exception.CommunicationError as e:
        return "CommunicationError" + str(e.key)
        pass
    except Exception as e:
        return str(e)

def callFunctionModule(conn, functionName, callParams) -> dict:
    try:
        result = conn.call(functionName, options={"timeout": 10}, **callParams)
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

def deleteFunctionModule(conn, functionName):
    conn.call("Z_FUNCTION_DELETE", FUNCNAME=functionName)
