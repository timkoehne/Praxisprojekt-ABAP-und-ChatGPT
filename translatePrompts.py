import json
import os
#from googletrans import Translator
from chatGptWrapper import ChatGPT


def readHumanEval():
    with open("human-eval-v2-20210705.json", encoding="utf-8") as file:
        content = json.loads(file.read())
    return content

def writePromptsToFiles(prompts):
    for index, x in enumerate(prompts):
        filename = "prompts/" + str(index) + ".txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(x)
    
def translatePrompts(): 
    files = os.listdir("only prompts/")
    alreadyTranslated = os.listdir("translated prompts/")
    for file in files:
        if file in alreadyTranslated:
            continue
        with open("only prompts/"+file, "r", encoding="utf-8") as readfile:
            prompt = readfile.read()
            # translation = translator.translate(prompt, dest='de', src='en').text
            translation = chatgpt.askWithoutContext(prompt)
            print("translating " + file)
            # print("\"" + prompt + "\" translated is \"" + translation + "\"")
            with open("translated prompts/"+ file, "w", encoding="utf-8") as writefile:
                writefile.write(translation)
                
def saveModifiedJson(humaneval):
    newEntries = []
    files = os.listdir("translated prompts/")
    for index, file in enumerate(files):
        with open("translated prompts/" + file, "r", encoding="utf-8") as readfile:
            newEntries.append(
                    {
                        "task_id": file.removesuffix(".txt"), 
                        "prompt": readfile.read(),
                        "canonical_solution": humaneval[index]["canonical_solution"], 
                        "test": humaneval[index]["test"]
                    }
                )
    
    with open("translated prompts.json", "w") as writefile:
        writefile.write(json.dumps(newEntries, indent=4))


# translator = Translator()
chatgpt = ChatGPT("translate to german")
humaneval = readHumanEval()

##run these each seperatly to manually edit / verify the prompts between functions
#writePromptsToFiles([ x["prompt"] for x in humaneval ])
#translatePrompts()
#saveModifiedJson(humaneval)