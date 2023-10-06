import json

class Model():
    def __init__(self, name: str, pricingPer1000: float):
        self.name = name
        self.pricingPer1000 = pricingPer1000


with open("human-eval-v2-20210705.json") as file:
    content = json.loads(file.read())

charsPerToken = 4
numberOfTests = 100
prompts = { x["prompt"] for x in content}
numPrompts = len(prompts)
averageCharsPerPrompt = sum({len(x) for x in prompts}) / numPrompts
averageTokenPerPrompt = averageCharsPerPrompt/charsPerToken

models = [Model("ChatGPT", 0.002),
          Model("Gpt4", 0.03)]

print("HumanEval has {} task".format(numPrompts))
print("HumanEval has on average {:.2f} characters per task".format(averageCharsPerPrompt))
print("HumanEval has on average {:.2f} tokens per task".format(averageTokenPerPrompt))


for model in models:
    averageCostPerPrompt = averageTokenPerPrompt/1000 * model.pricingPer1000
    overallCost = averageCostPerPrompt * numPrompts
    print("--------{}--------".format(model.name))
    print("{} costs about {:.3f}€ per 1000 Tokens".format(model.name, model.pricingPer1000))
    print("The price will on average be {:.4f}€ per prompt".format(averageCostPerPrompt))
    print("The price for running all prompts once will be {:.2f}€".format(overallCost))
    print("Expect {:.2f}€ since the answers also cost money".format(overallCost*2))
    print("The price for {} repetitions on all prompts will be {:.2f}€".format(numberOfTests, overallCost*numberOfTests))
    print("Expect {:.2f}€ since the answers also cost money".format((overallCost*numberOfTests)*2))
    
for x in prompts:
    print(x)