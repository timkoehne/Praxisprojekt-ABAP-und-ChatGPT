import openai

#load api key
with open("openAiApiKey.txt", "r") as file:
    apiKey = file.read()
openai.api_key = apiKey

#generate response
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0.0, # 0 to 2
    max_tokens = 2048,
    messages=[ # roles can be user, assistant, system
        {"role": "system", "content": "only generate standalone abap functions without explanations or examples"},
        {"role": "user", "content": "how do i calculate the fibonacci sequence"},
    ],
)

response: str = completion.choices[0].message.content  # type: ignore
print(response)
