import json

def analysePrompts(loadfilename):    
    with open(loadfilename, "r") as file:
        prompts = json.loads(file.read())

    numFunctionsCreated = 0
    numUnitTestsPassed = 0
    numUnitTests = 0
    numSuccessful = 0
    numAttempts = 0
    statusList = {}
    exceptionsList = {}
    successfulList = []
    
    for systemPromptIndex, systemPrompt in enumerate(prompts):
        for tempIndex, temperature in enumerate(prompts[systemPrompt]):
            for promptOptionIndex, promptOption in enumerate(prompts[systemPrompt][temperature]):
                for promptNumber in prompts[systemPrompt][temperature][promptOption]:
                    for attemptNr, attempt in enumerate(prompts[systemPrompt][temperature][promptOption][promptNumber]["attempts"]):
                        currentAttempt = prompts[systemPrompt][temperature][promptOption][promptNumber]["attempts"][attemptNr]
                        numAttempts += 1
                        numUnitTests+=attempt["tests"]
                        numUnitTestsPassed+=attempt["passed"]
                        for call in attempt["functionCalls"]:
                        
                            status = list(call.items())[0][0] if len(list(call.items())) > 0 else "empty return value"
                            item: str = list(call.items())[0][1] if len(list(call.items())) > 0 else "empty return value"
                            
                            if status == "exception":
                                if item.startswith('ExternalRuntimeError("field \'REFERENCE('):
                                    item = 'ExternalRuntimeError("field \'REFERENCE(x)\' not found")'
                                elif item.startswith('ExternalRuntimeError("field \''):
                                    item = 'ExternalRuntimeError("field \'x\' not found")'
                                elif item.startswith('FunctionCall: RuntimeError 3 (rc=3): key=CALL_FUNCTION_NOT_FOUND'):
                                    item = "FunctionCall: RuntimeError 3 (rc=3): key=CALL_FUNCTION_NOT_FOUND"
                                elif item.startswith('FunctionCall: TypeError: '):
                                    item = "FunctionCall: TypeError"
                                statusList[status] = statusList.get(status, 0) + 1
                                exceptionsList[item] = exceptionsList.get(item, 0) + 1
                                break
                            
                        if attempt["tests"] == attempt["passed"]:
                            numSuccessful += 1
                            successfulList.append({"systemPrompt": systemPrompt, "temperature": temperature, "promptOption": promptOption, "promptNumber": promptNumber, "attemptNr": attemptNr})
                        if attempt["functionCreated"] == "success":
                            numFunctionsCreated+=1
        
        
    print(str(numFunctionsCreated) + " out of " + str(numAttempts) + " functions were successfully created")
    print(str(numUnitTestsPassed) + " out of " + str(numUnitTests) + " unit-tests were successful")
    print(str(numSuccessful) + " out of " + str(numAttempts) + " tests were successful")

    print("-----Total Errors-----")
    for key, value in statusList.items():
        print(str(value) + "x " + str(key))
    print("-----Exceptions-----")
    for key, value in sorted(exceptionsList.items(), key=lambda item: item[1], reverse=True):
        print(str(value) + "x " + str(key))

    print("-----Successful Attempts-----")
    for attempt in successfulList:
        print(attempt)
        
    print(len(successfulList))

def analysePromptsTestParameter(loadfilename):    
    with open(loadfilename, "r") as file:
        prompts = json.loads(file.read())
    
    summedFunctionsCreated = 0
    summedSuccessful = 0
    
    for systemPromptIndex, systemPrompt in enumerate(prompts):
        for tempIndex, temperature in enumerate(prompts[systemPrompt]):
            for promptOptionIndex, promptOption in enumerate(prompts[systemPrompt][temperature]):
                
                numFunctionsCreated = 0
                numUnitTestsPassed = 0
                numUnitTests = 0
                numSuccessful = 0
                numAttempts = 0
                statusList = {}
                exceptionsList = {}
                successfulList = []
                
                for promptNumber in prompts[systemPrompt][temperature][promptOption]:
                    for attemptNr, attempt in enumerate(prompts[systemPrompt][temperature][promptOption][promptNumber]["attempts"]):
                        currentAttempt = prompts[systemPrompt][temperature][promptOption][promptNumber]["attempts"][attemptNr]
                        numAttempts += 1
                        numUnitTests+=attempt["tests"]
                        numUnitTestsPassed+=attempt["passed"]
                        for call in attempt["functionCalls"]:
                        
                            status = list(call.items())[0][0] if len(list(call.items())) > 0 else "empty return value"
                            item: str = list(call.items())[0][1] if len(list(call.items())) > 0 else "empty return value"
                            
                            if status == "exception":
                                if item.startswith('ExternalRuntimeError("field \'REFERENCE('):
                                    item = 'ExternalRuntimeError("field \'REFERENCE(x)\' not found")'
                                elif item.startswith('ExternalRuntimeError("field \''):
                                    item = 'ExternalRuntimeError("field \'x\' not found")'
                                elif item.startswith('FunctionCall: RuntimeError 3 (rc=3): key=CALL_FUNCTION_NOT_FOUND'):
                                    item = "FunctionCall: RuntimeError 3 (rc=3): key=CALL_FUNCTION_NOT_FOUND"
                                elif item.startswith('FunctionCall: TypeError: '):
                                    item = "FunctionCall: TypeError"
                                statusList[status] = statusList.get(status, 0) + 1
                                exceptionsList[item] = exceptionsList.get(item, 0) + 1
                                break
                            
                        if attempt["tests"] == attempt["passed"]:
                            numSuccessful += 1
                            successfulList.append({"systemPrompt": systemPrompt, "temperature": temperature, "promptOption": promptOption, "promptNumber": promptNumber, "attemptNr": attemptNr})
                        if attempt["functionCreated"] == "success":
                            numFunctionsCreated+=1
                
                
                if promptOptionIndex == 2: #TODO manually change this to each parameter and value to add only the relevants
                    summedFunctionsCreated += numFunctionsCreated
                    summedSuccessful += numSuccessful
                    print("Systemprompt: ", systemPromptIndex, "temperature: ", tempIndex, "promptOption: ", promptOptionIndex)
                    print(str(numFunctionsCreated) + " out of " + str(numAttempts) + " functions were successfully created")
                    print(str(numUnitTestsPassed) + " out of " + str(numUnitTests) + " unit-tests were successful")
                    print(str(numSuccessful) + " out of " + str(numAttempts) + " tests were successful")

                    # print("-----Total Errors-----")
                    # for key, value in statusList.items():
                    #     print(str(value) + "x " + str(key))
                    # print("-----Exceptions-----")
                    # for key, value in sorted(exceptionsList.items(), key=lambda item: item[1], reverse=True):
                    #     print(str(value) + "x " + str(key))

                    print("-----Successful Attempts-----")
                    for attempt in successfulList:
                        print(attempt)
        
    print("summedFunctionsCreated " + str(summedFunctionsCreated))
    print("summedSuccessful " + str(summedSuccessful))

