import json

def removeRunDetails(filename: str):
    with open(filename) as file:
        prompts = json.loads(file.read())
    
    for systemPromptIndex, systemPrompt in enumerate(prompts):
        for tempIndex, temperature in enumerate(prompts[systemPrompt]):
            for promptOptionIndex, promptOption in enumerate(prompts[systemPrompt][temperature]):
                for promptNumber in prompts[systemPrompt][temperature][promptOption]:
                    for attemptNr, attempt in enumerate(prompts[systemPrompt][temperature][promptOption][promptNumber]["attempts"]):
                        currentAttempt = prompts[systemPrompt][temperature][promptOption][promptNumber]["attempts"][attemptNr]
                        
                        if "functionname" in currentAttempt: del currentAttempt["functionname"]
                        if "importParameters" in currentAttempt: del currentAttempt["importParameters"]
                        if "exportParameters" in currentAttempt: del currentAttempt["exportParameters"]
                        if "programcode" in currentAttempt: del currentAttempt["programcode"]
                        if "functionCreated" in currentAttempt: del currentAttempt["functionCreated"]
                        if "passed" in currentAttempt: del currentAttempt["passed"]
                        if "failed" in currentAttempt: del currentAttempt["failed"]
                        if "tests" in currentAttempt: del currentAttempt["tests"]
                        if "functionCalls" in currentAttempt: del currentAttempt["functionCalls"]
                        
                        prompts[systemPrompt][temperature][promptOption][promptNumber]["attempts"][attemptNr] = currentAttempt
                        
                        
                        
    with open(filename, "w") as file:
        file.write(json.dumps(prompts, indent=4))

def combineJsons(loadfilename1, loadfilename2, savefilename: str):
    with open(loadfilename1) as file:
        prompts1 = json.loads(file.read())
    with open(loadfilename2) as file:
        prompts2 = json.loads(file.read())
        
    merged = {}
    
    for systemPromptIndex, systemPrompt in enumerate(prompts1):
        if systemPrompt not in merged: merged[systemPrompt] = {}
        for tempIndex, temperature in enumerate(prompts1[systemPrompt]):
            if temperature not in merged[systemPrompt]: merged[systemPrompt][temperature] = {}
            for promptOptionIndex, promptOption in enumerate(prompts1[systemPrompt][temperature]):
                if promptOption not in merged[systemPrompt][temperature] : merged[systemPrompt][temperature][promptOption] = {}
                for promptNumber in prompts1[systemPrompt][temperature][promptOption]:
                    if promptNumber not in merged[systemPrompt][temperature][promptOption] : merged[systemPrompt][temperature][promptOption][promptNumber] = {"attempts": []}
                    for attemptNr, attempt in enumerate(prompts1[systemPrompt][temperature][promptOption][promptNumber]["attempts"]):
                        merged[systemPrompt][temperature][promptOption][promptNumber]["attempts"].append(attempt)
                        
    for systemPromptIndex, systemPrompt in enumerate(prompts2):
        if systemPrompt not in merged: merged[systemPrompt] = {}
        for tempIndex, temperature in enumerate(prompts2[systemPrompt]):
            if temperature not in merged[systemPrompt]: merged[systemPrompt][temperature] = {}
            for promptOptionIndex, promptOption in enumerate(prompts2[systemPrompt][temperature]):
                if promptOption not in merged[systemPrompt][temperature] : merged[systemPrompt][temperature][promptOption] = {}
                for promptNumber in prompts2[systemPrompt][temperature][promptOption]:
                    if promptNumber not in merged[systemPrompt][temperature][promptOption] : merged[systemPrompt][temperature][promptOption][promptNumber] = {"attempts": []}
                    for attemptNr, attempt in enumerate(prompts2[systemPrompt][temperature][promptOption][promptNumber]["attempts"]):
                        merged[systemPrompt][temperature][promptOption][promptNumber]["attempts"].append(attempt)
                        
    with open(savefilename, "w") as file:
        file.write(json.dumps(merged, indent=4))
