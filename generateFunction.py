from chatGptWrapper import ChatGPT

question = """add \"by john smith\" to the end of the string and return it"""


chatgpt = ChatGPT(systemMessage="always generate a abap function module including the interface. no explanations or examples.")
answer = chatgpt.askWithoutContext(question)

with open("answer.txt", "w") as file:
    file.write(answer)



