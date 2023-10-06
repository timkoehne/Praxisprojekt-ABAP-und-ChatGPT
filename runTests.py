import rfcMethod
import analyseTestResults

# #-----------GPT4------------
# systemPromptOptions = ["generate a abap function module. no explanations or examples."]
# promptOptions = ["prompts without examples/"]
# temperatureOptions = [0]
# promptsToRun = [0, 6, 13, 15, 24, 27, 28, 34, 35, 37, 40, 41, 44, 47, 48, 49, 56, 61,
#                 62, 65, 67, 70, 77, 78, 84, 89, 90, 94, 104, 117, 119, 123, 135, 137, 145,
#                 148, 154, 156, 157, 158]
# numRepeats = 3
# numThreads = 3
# rfcMethod.askChatGptForPromptsMultithreaded("results/gpt4.json", systemPromptOptions, promptOptions, temperatureOptions, "gpt-4", promptsToRun, numRepeats, numThreads)
# rfcMethod.runSavedFunctions("results/gpt4.json", "results/gpt4-Processed.json")
# analyseTestResults.analysePrompts("results/gpt4-Processed.json")

# # #-----------Translated------------
# systemPromptOptions = ["generiere einen abap funktionsbaustein. keine erklärungen oder beispiele."]
# promptOptions = ["translated prompts without examples/"]
# temperatureOptions = [0]
# promptsToRun = [0, 6, 13, 15, 24, 27, 28, 34, 35, 37, 40, 41, 44, 47, 48, 49, 56, 61,
#                 62, 65, 67, 70, 77, 78, 84, 89, 90, 94, 104, 117, 119, 123, 135, 137, 145,
#                 148, 154, 156, 157, 158]
# numRepeats = 3
# numThreads = 7
# rfcMethod.askChatGptForPromptsMultithreaded("results/translated.json", systemPromptOptions, promptOptions, temperatureOptions, "gpt-3.5-turbo", promptsToRun, numRepeats, numThreads)
# rfcMethod.runSavedFunctions("results/translated.json", "results/translated-Processed.json")
# analyseTestResults.analysePrompts("results/translated-Processed.json")

# # #-----------find parameters------------
# systemPromptOptions = ["generate a abap function module. no explanations or examples.",
#     "generate a abap function module including the interface comment. no explanations or examples.",
#     "generate a abap function module including the interface comment with IMPORTING and EXPORTING. no explanations or examples."]
# promptOptions = ["prompts/",
#     "prompts only text/",
#     "prompts without examples/"]
# temperatureOptions = [0, 0.8, 2]
# promptsToRun = [0, 6, 13, 15, 24, 27, 28, 34, 35, 37, 40, 41, 44, 47, 48, 49, 56, 61,
#                 62, 65, 67, 70, 77, 78, 84, 89, 90, 94, 104, 117, 119, 123, 135, 137, 145,
#                 148, 154, 156, 157, 158]
# numRepeats = 3
# numThreads = 5

# rfcMethod.askChatGptForPromptsMultithreaded("results/findParameters.json", systemPromptOptions, promptOptions, temperatureOptions, "gpt-3.5-turbo", promptsToRun, 3, 5)
# rfcMethod.runSavedFunctions("results/findParameters.json", "results/findParameters-Processed.json")
# analyseTestResults.analysePromptsTestParameter("results/findParameters-Processed.json")


# # #-----------big run------------
# systemPromptOptions = ["generate a abap function module. no explanations or examples."]
# promptOptions = ["prompts without examples/"]
# temperatureOptions = [0]
# promptsToRun = [i for i in range(0, 164)]
# numRepeats = 3
# numThreads = 5

# rfcMethod.askChatGptForPromptsMultithreaded("results/bigRun.json", systemPromptOptions, promptOptions, temperatureOptions, "gpt-3.5-turbo", promptsToRun, 3, 5)
# rfcMethod.runSavedFunctions("results/bigRun.json", "results/bigRun-Processed.json")
# analyseTestResults.analysePrompts("results/bigRun-Processed")



