import openai

class ChatGPT:
    def __init__(self, systemMessage="") -> None:
        self.context = []
        self.systemMessage = systemMessage
        with open("openAiApiKey.txt", "r") as file:
            apiKey = file.read()
            openai.api_key = apiKey

    def _runQuery(self, messages):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.0, # 0 to 2
            max_tokens = 2048,
            messages=messages
        )
        return completion.choices[0].message.content  # type: ignore

    def askWithoutContext(self, userMessage):
        messages = []
        if self.systemMessage != "":
            messages.append({"role": "system", "content": self.systemMessage})
        messages.append({"role": "user", "content": userMessage})

        response = self._runQuery(messages)
        return response
    
    def askWithContext(self, userMessage):
        messages = []
        if self.systemMessage != "":
            messages.append({"role": "system", "content": self.systemMessage})
        for message in self.context:
            messages.append(message)
        messages.append({"role": "user", "content": userMessage})
        
        response = self._runQuery(messages)
        self.context.append({"role": "assistant", "content": response})
        return response