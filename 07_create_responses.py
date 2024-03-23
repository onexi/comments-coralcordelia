import openai
import sqlite3
import json

size_processed = 10

key = "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"
openai.api_key = key

con = sqlite3.connect('comments.db')
cur = con.cursor()
cur.execute("SELECT * FROM comments")
comments = cur.fetchmany(size = size_processed)[1:]

combined_comments_and_responses = []

for comment in comments:
    if comment[-1] == 1 or comment[-1] == '1':
        message_to_send_to_ai = {
            "role": "user",
            "content": f"""I have a comment on a video about Sam Altman's interview concerning ChatGPT-4. 
            Please write a response to this comment. If the comment expresses concerns towards the interview, Sam Altman, 
            OpenAI, or AI in general, make sure you address the user and acknowledge their concerns,
            but that you ultimately accurately respond to criticism about Sam Altman and the interview. To comments speaking
            complimenting the interview, be sure to thank the user. Remember to keep the comment brief. Here is the comment, typed by {comment[3]}: {comment[1]}.
            """
        }
        message = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [message_to_send_to_ai])
        response = message.choices[0].message.content.strip()
        combined_comments_and_responses.append((message, comment))
        print(f'Comment: {comment[1]}\n Response: {response}')



