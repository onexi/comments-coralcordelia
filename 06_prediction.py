import openai
import sqlite3
import json

key = "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"
openai.api_key = key

con = sqlite3.connect('comments.db')
cur = con.cursor()
cur.execute("SELECT * FROM comments")
comments = cur.fetchmany(size = 10)[1:]

responses = []

for ind, comment in enumerate(comments):
    print(f'Current comment processed: Comment {ind + 1}: {comment[1]}')
    message_to_send = {
        "role": "user",
        "content": """I have a comment on a video about Sam Altman's interview concerning ChatGPT-4. 
Please return a JSON dictionary with keys "angry", "negative", "response", and "spam", with each key assigned to a boolean value, based on the following:
\nTo "angry", assign true if the comment is angry; otherwise, assign false. 
\nTo "negative", assign true if the comment is negative; otherwise, assign false. 
\nTo "response", assign true if the comment warrants a response; otherwise, assign false. For this one, please follow the following steps:
\n1. Is the comment relevant to the interview?
\n2. If so, does the comment express or ask for a meaningful point of view which facilitates discussion about AI?
\n3. If so, does the comment's tone indicate a serious tone open to dialogue, as opposed to a sarcastic tone meant to make fun of Altman or the interview?
\n4. Does the comment open a discussion? Many comments may make relevant remarks to the video, but not necessarily open a discussion.
\nIf any of these four are false, you should return talse for the property "response."
\n
\nTo "spam", assign true if and only if the comment is irrelevant to the topics of AI, Lex Fridman's channel, and/or the interview. Comments talking vaguely about the interview or any of these topics should not be flagged as spam. 
If you're unsure, please try to err on assigning this as false.
\n
\nHere is the comment: """ + comment[1] + """
\nPlease return the dictionary in a JSON format, and not anything else.
"""
    }
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [message_to_send])
    choice = response.choices[0].message.content.strip()
    responses.append((choice, comment))
    print(f'Response: {choice}')


cleaned_responses = [(json.loads(response), comment) for (response, comment) in responses]

cur.executemany("""UPDATE comments
                SET (negative, angry, spam, response) = (?, ?, ?, ?)
                WHERE cid = ?""", [(response['negative'], response['angry'], response['spam'], response['response'], comment[0]) for (response, comment) in cleaned_responses])

con.commit()