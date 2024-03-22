import openai
import sqlite3
import json

key = ""
openai.api_key = key

response = openai.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hi!"}
    ]
)