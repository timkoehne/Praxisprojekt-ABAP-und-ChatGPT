
import importlib
import json
import more_itertools
import pyrfc
import threading
import queue
import time
import pythonAbapInterface

from chatGptWrapper import ChatGPT

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
class ChatGPTRequest():
    def __init__(self, systemPrompt, promptOption, temperature, promptNumber) -> None:
        self.systemPrompt = systemPrompt
        self.promptOption = promptOption
        self.temperature = temperature
        self.promptNumber = promptNumber
class ChatGPTResponse():
    def __init__(self, request: ChatGPTRequest, chatgptResponse: list[str]) -> None:
        self.request: ChatGPTRequest = request
        self.chatgptResponse: list[str] = chatgptResponse
        
    def __str__(self) -> str:
        return self.request.systemPrompt + " " + self.request.promptOption +  " " + str(self.request.temperature) + " " + str(self.request.promptNumber) + " " + self.chatgptResponse

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

def askChatGptForPromptsSingleThread(savefilename: str, threadId: int, openaiModel: str, requestList: list[ChatGPTRequest], q: queue.Queue):
    if savefilename.endswith(".json"): savefilename = savefilename.removesuffix(".json")
    progressCounter = 0
    
    saveDict = {}
    
    for request in requestList:
        chatgpt = ChatGPT(systemMessage=request.systemPrompt, temperature=request.temperature, model=openaiModel)

        if request.systemPrompt not in saveDict: 
            saveDict[request.systemPrompt] = {}
        if str(request.temperature) not in saveDict[request.systemPrompt]: 
            saveDict[request.systemPrompt][str(request.temperature)] = {}
        if request.promptOption not in saveDict[request.systemPrompt][str(request.temperature)]: 
            saveDict[request.systemPrompt][str(request.temperature)][request.promptOption] = {}
        if str(request.promptNumber) not in saveDict[request.systemPrompt][str(request.temperature)][request.promptOption]: 
            saveDict[request.systemPrompt][str(request.temperature)][request.promptOption][str(request.promptNumber)] = {}
        if "attempts" not in saveDict[request.systemPrompt][str(request.temperature)][request.promptOption][str(request.promptNumber)]: 
            saveDict[request.systemPrompt][str(request.temperature)][request.promptOption][str(request.promptNumber)]["attempts"] = []
        
        prompt = getPrompt(request.promptOption, request.promptNumber)
        saveDict[request.systemPrompt][str(request.temperature)][request.promptOption][str(request.promptNumber)]["prompt"] = prompt
        
        saveTo = {}
        chatgptResponse = None
        tries = 0
        while chatgptResponse == None and tries < 10:
            try:
                chatgptResponse = chatgpt.askWithoutContext(prompt).split("\n")
            except Exception:
                chatgptResponse = None
                print("Thread", threadId, "crashed", tries, "times, retrying in 5 seconds")
                tries += 1
                time.sleep(5)
        saveTo["chatgptResponse"] = chatgptResponse
        saveDict[request.systemPrompt][str(request.temperature)][request.promptOption][str(request.promptNumber)]["attempts"].append(saveTo)
        progressCounter += 1
        print("Thread " + str(threadId) + " Progress " + str(progressCounter) + "/" + str(len(requestList)))
        
        
        if (progressCounter.__mod__(50) == 0):
            with open("backup/" + savefilename + " thread" + str(threadId) + " progress" + str(progressCounter) + ".json", "w") as file:
                file.write(json.dumps(saveDict, indent=4))
        
        time.sleep(5)
    with open("backup/" + savefilename + " thread" + str(threadId) + " progress" + str(progressCounter) + ".json", "w") as file:
        file.write(json.dumps(saveDict, indent=4))
        
    q.put(saveDict)

def askChatGptForPromptsMultithreaded(savefilename: str, systemPrompts, promptOptions, temperatures, openaiModel, promptNumbers: list[int], numRepeats: int, numThreads: int):
    saveDict = {}
    requests: list[ChatGPTRequest] = []

    # initialize dict
    for systemPrompt in systemPrompts:
        saveDict[systemPrompt] = {}
        for temperature in temperatures:
            saveDict[systemPrompt][str(temperature)] = {}
            for promptOption in promptOptions:
                saveDict[systemPrompt][str(temperature)][promptOption] = {}
                for promptNumber in promptNumbers:
                    saveDict[systemPrompt][str(temperature)][promptOption][str(promptNumber)] = {}
                    prompt = getPrompt(promptOption, promptNumber)
                    saveDict[systemPrompt][str(temperature)][promptOption][str(promptNumber)]["prompt"] = prompt
                    saveDict[systemPrompt][str(temperature)][promptOption][str(promptNumber)]["attempts"] = []
                    for repeat in range(0, numRepeats):
                        requests.append(ChatGPTRequest(systemPrompt, promptOption, temperature, promptNumber))
    
    # calculate which thread does what
    numAllIterations = len(systemPrompts) * len(promptOptions) * len(temperatures) * len(promptNumbers) * numRepeats
    numThreads = min(numThreads, numAllIterations)
    print("distributing", numAllIterations, "prompts to", numThreads, "threads")
    threadLists = [list(i) for i in more_itertools.divide(numThreads, requests)]

    # print(len(threadLists))
    # for thread in threadLists:
    #     print(thread)
        # for item in thread:
        #     print(item)
    
    # start threads
    q = queue.Queue()
    pool = []
    for index, requestList in enumerate(threadLists):
        print("creating thread " + str(index))
        t = threading.Thread(target=askChatGptForPromptsSingleThread, args=(savefilename, index, openaiModel, requestList, q))
        t.start()
        pool.append(t)
        
    # save thread data
    for index, t in enumerate(pool):
        t.join()
        response = q.get()
        responseSystemPrompts = list(response.keys())
        for responseSystemPrompt in responseSystemPrompts:
            responseTemperatures = list(response[responseSystemPrompt].keys())
            for responseTemperature in responseTemperatures:
                responsePromptOptions = list(response[responseSystemPrompt][responseTemperature].keys())
                for responsePromptOption in responsePromptOptions:
                    responsePromptNums = list(response[responseSystemPrompt][responseTemperature][responsePromptOption].keys())
                    for responsePromptNum in responsePromptNums:
                        responseAttempts = response[responseSystemPrompt][responseTemperature][responsePromptOption][responsePromptNum]["attempts"]
                        # print(responseAttempts)
                        for attempt in responseAttempts:
                            saveDict[responseSystemPrompt][str(responseTemperature)][responsePromptOption][responsePromptNum]["attempts"].append(attempt)

    with open(savefilename, "w") as file:
        file.write(json.dumps(saveDict, indent=4))

def runSavedFunctions(loadfilename: str, savefilename: str):
    if savefilename.endswith(".json"): savefilename = savefilename.removesuffix(".json")
    with open(loadfilename) as file:
        prompts = json.loads(file.read())
    
    with open("saplogonLoginDetails - local.json", "r") as file:
        connection_params = json.loads(file.read())
    
    progressCounter = 0

    for systemPromptIndex, systemPrompt in enumerate(prompts):
        for tempIndex, temperature in enumerate(prompts[systemPrompt]):
            for promptOptionIndex, promptOption in enumerate(prompts[systemPrompt][temperature]):
                for promptNumber in prompts[systemPrompt][temperature][promptOption]:
                    for attemptNr, attempt in enumerate(prompts[systemPrompt][temperature][promptOption][promptNumber]["attempts"]):
                        currentAttempt = prompts[systemPrompt][temperature][promptOption][promptNumber]["attempts"][attemptNr]
                        progressCounter += 1
                        print("Progress: ", str(progressCounter), "/", str(len(prompts) *
                                                                    len(prompts[systemPrompt]) *
                                                                    len(prompts[systemPrompt][temperature]) *
                                                                    len(prompts[systemPrompt][temperature][promptOption]) *
                                                                    len(prompts[systemPrompt][temperature][promptOption][promptNumber]["attempts"])))
                        if "functionname" not in currentAttempt:
                            try:
                                functionName, importParameters, exportParameters, programcode = extractAbapFunctionInformation(currentAttempt["chatgptResponse"])
                            except Exception as e:
                                functionName, importParameters, exportParameters, programcode = "defaultFunctionName", "", "", ""
                                print(e)
                            
                            currentAttempt["functionname"] = functionName
                            currentAttempt["importParameters"] = importParameters
                            currentAttempt["exportParameters"] = exportParameters
                            currentAttempt["programcode"] = programcode
                            
                            with pyrfc.Connection(**connection_params) as conn:
                                functionCreated = pythonAbapInterface.createFunctionModule(conn, 
                                                                        currentAttempt["functionname"],
                                                                        currentAttempt["importParameters"],
                                                                        currentAttempt["exportParameters"],
                                                                        currentAttempt["programcode"])
                                
                                currentAttempt["functionCreated"] = functionCreated
                                time.sleep(1)
                                testModule = importlib.import_module("adjustedTests.test" + str(promptNumber))
                                passed, failed = testModule.check(Test(conn, 
                                                                        currentAttempt["functionname"],
                                                                        currentAttempt["importParameters"],
                                                                        currentAttempt["exportParameters"],
                                                                        currentAttempt).callFunction)
                                currentAttempt["passed"] = passed
                                currentAttempt["failed"] = failed
                                currentAttempt["tests"] = passed+failed
                                print(f"Prompt {promptNumber} Attempt {attemptNr}: {passed} out of {passed+failed} unit-tests were successful")
                                
                            with pyrfc.Connection(**connection_params) as conn:
                                pythonAbapInterface.deleteFunctionModule(conn, currentAttempt["functionname"])
                            prompts[systemPrompt][str(temperature)][promptOption][str(promptNumber)]["attempts"][attemptNr] = currentAttempt
                            
                            
                            if (progressCounter.__mod__(50) == 0):
                                with open("backup/" + savefilename + " progress" + str(progressCounter) + ".json", "w") as file:
                                    file.write(json.dumps(prompts, indent=4))
                                
    with open(savefilename + ".json", "w") as file:
        file.write(json.dumps(prompts, indent=4))