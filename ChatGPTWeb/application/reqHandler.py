import openai

openai.api_key = "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"
model_engine = "text-davinci-002"

def getAnswer(prompt):
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.9, max_tokens=1024)
    return response
