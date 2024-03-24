import openai
import sqlite3
import json

key = "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"
openai.api_key = key

con = sqlite3.connect('comments.db')
cur = con.cursor()
cur.execute("SELECT * FROM comments")
comments = cur.fetchmany(size = 100)

combined_comments_and_responses = []

for (ind, comment) in enumerate(comments):
    try:
        print(f'Currently processing comment {ind}')
        message_to_send_to_ai = {
            "role": "user",
            "content": f"""
            I have a comment on a video about Sam Altman's interview concerning ChatGPT-4. 
            Please return a JSON dictionary with keys "ethical", "compliment", "personal", "hyperbolic", and "interview", with each key assigned to a boolean value, based on the following:
            \nTo "ethical", assign true if the comment raises ethical concerns about Sam Altman, ChatGPT, OpenAI, or AI in general.
            \nTo "compliment", assign true if the comment compliments Lex Fridman
            \nTo "personal", assign true if the comment is directed more about Altman personally than about him in the context of OpenAI.
            \nTo "hyperbolic", assign true if the comment uses hyperbolic or exaggerated language.
            \nTo "interview", assign true if the comment is talking about a specific part of the interview. Assign false if the comment talks more broadly about Altman, ChatGPT, or AI.
            Please remember to return this as a JSON dictionary, with keys "ethical", "compliment", "personal", "hyperbolic", and "interview".
            """
        }
        message = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [message_to_send_to_ai])
        response = message.choices[0].message.content.strip()
        combined_comments_and_responses.append((json.loads(response), comment))
    except:
        print('Exception occured')

# cur.execute("""
#     ALTER TABLE comments
#     ADD ethical INT
# """)
# cur.execute("""
#     ALTER TABLE comments
#     ADD compliment INT
# """)
# cur.execute("""
#     ALTER TABLE comments
#     ADD personal INT
# """)
# cur.execute("""
#     ALTER TABLE comments
#     ADD hyperbolic INT
# """)
# cur.execute("""
#     ALTER TABLE comments
#     ADD interview INT
# """)

cur.executemany("""UPDATE comments
                SET (ethical, compliment, personal, hyperbolic, interview) = (?, ?, ?, ?, ?)
                WHERE cid = ?""", [(response['ethical'], response['compliment'], response['personal'], response['hyperbolic'], response['interview'], comment[0]) for (response, comment) in combined_comments_and_responses])


con.commit()