import openai

key = "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"
openai.api_key = key

response = openai.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "user", "content": "How many states are there in the United States of America?"}
    ]
)
msg = response.choices[0].message.content.strip()
returned_value = {
    "answer": msg
}
print(returned_value)