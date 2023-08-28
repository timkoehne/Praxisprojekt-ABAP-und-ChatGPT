from time import sleep
import openai
import openai.error


retryTime = 5

class ChatGPT:
    def __init__(self, systemMessage="", temperature=0.8, model="gpt-3.5-turbo") -> None:
        self.context = []
        self.systemMessage = systemMessage
        self.temperature = temperature
        self.model = model
        with open("openAiApiKey.txt", "r") as file:
            apiKey = file.read()
            openai.api_key = apiKey

    def _runQuery(self, messages):
        
        attempts = 0
        completion = ""
        while completion == "" and attempts <= 10:
            try:
                completion = openai.ChatCompletion.create(
                    model=self.model,
                    temperature=self.temperature, # 0 to 2
                    max_tokens = 2048,
                    messages=messages)
                    
            except (openai.error.APIError, openai.error.ServiceUnavailableError) as e:
                attempts += 1
                print(e)
                print(f"OpenAI APIError: trying again in {retryTime} seconds...")
                sleep(retryTime)
            
            if attempts > 10:
                return "OpenAI APIError"
        return completion.choices[0].message.content  # type: ignore

    def askWithoutContext(self, userMessage):
        messages = []
        if self.systemMessage != "":
            messages.append({"role": "system", "content": self.systemMessage})
        messages.append({"role": "user", "content": userMessage})

        response = self._runQuery(messages)
        return str(response)
    
    def askWithContext(self, userMessage):
        messages = []
        if self.systemMessage != "":
            messages.append({"role": "system", "content": self.systemMessage})
        for message in self.context:
            messages.append(message)
        messages.append({"role": "user", "content": userMessage})
        
        response = self._runQuery(messages)
        self.context.append({"role": "assistant", "content": response})
        return str(response)
    
    def listModels(self):
        models = openai.Model.list()
        if isinstance(models, dict):
            return [i["id"] for i in models["data"]]
        
        