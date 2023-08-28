import rfcMethod
import analyseTestResults

# #-----------GPT4------------
systemPromptOptions = ["generate a abap function module. no explanations or examples."]
promptOptions = ["prompts without examples/"]
temperatureOptions = [0]
promptsToRun = [0, 6, 13, 15, 24, 27, 28, 34, 35, 37, 40, 41, 44, 47, 48, 49, 56, 61,
                62, 65, 67, 70, 77, 78, 84, 89, 90, 94, 104, 117, 119, 123, 135, 137, 145,
                148, 154, 156, 157, 158]
numRepeats = 3
numThreads = 3
rfcMethod.askChatGptForPromptsMultithreaded("gpt4-new.json", systemPromptOptions, promptOptions, temperatureOptions, "gpt-4", promptsToRun, numRepeats, numThreads)
rfcMethod.runSavedFunctions("gpt4-new.json", "gpt4-new-Processed.json")
analyseTestResults.analysePrompts("gpt4-new-Processed.json")

# #-----------Translated------------
systemPromptOptions = ["generate a abap function module. no explanations or examples.", "generiere einen abap funktionsbaustein. keine erklärungen oder beispiele."]
promptOptions = ["translated prompts without examples/"]
temperatureOptions = [0]
promptsToRun = [0, 6, 13, 15, 24, 27, 28, 34, 35, 37, 40, 41, 44, 47, 48, 49, 56, 61,
                62, 65, 67, 70, 77, 78, 84, 89, 90, 94, 104, 117, 119, 123, 135, 137, 145,
                148, 154, 156, 157, 158]
numRepeats = 3
numThreads = 7
rfcMethod.askChatGptForPromptsMultithreaded("translated.json", systemPromptOptions, promptOptions, temperatureOptions, "gpt-3.5-turbo", promptsToRun, numRepeats, numThreads)
rfcMethod.runSavedFunctions("translated.json", "translated-Processed.json")
analyseTestResults.analysePrompts("translated-Processed.json")

# #-----------find parameters------------
systemPromptOptions = ["generate a abap function module. no explanations or examples.",
    "generate a abap function module including the interface comment. no explanations or examples.",
    "generate a abap function module including the interface comment with IMPORTING and EXPORTING. no explanations or examples."]
promptOptions = ["prompts/",
    "prompts only text/",
    "prompts without examples/"]
temperatureOptions = [0, 0.8, 2]
promptsToRun = [0, 6, 13, 15, 24, 27, 28, 34, 35, 37, 40, 41, 44, 47, 48, 49, 56, 61,
                62, 65, 67, 70, 77, 78, 84, 89, 90, 94, 104, 117, 119, 123, 135, 137, 145,
                148, 154, 156, 157, 158]
numRepeats = 3
numThreads = 5

rfcMethod.askChatGptForPromptsMultithreaded("newSmallTestCombined.json", systemPromptOptions, promptOptions, temperatureOptions, "gpt-3.5-turbo", promptsToRun, 3, 5)
rfcMethod.runSavedFunctions("newSmallTestCombined.json", "newSmallTestCombined-Processed.json")
analyseTestResults.analysePromptsTestParameter("newSmallTestCombined-Processed.json")


# #-----------big run------------
systemPromptOptions = ["generate a abap function module. no explanations or examples."]
promptOptions = ["prompts without examples/"]
temperatureOptions = [0]
promptsToRun = [i for i in range(0, 164)]
numRepeats = 3
numThreads = 5

rfcMethod.askChatGptForPromptsMultithreaded("bigRun.json", systemPromptOptions, promptOptions, temperatureOptions, "gpt-3.5-turbo", promptsToRun, 3, 5)
rfcMethod.runSavedFunctions("bigRun.json", "bigRun-Processed.json")
analyseTestResults.analysePromptsTestParameter("bigRun-Processed.json")