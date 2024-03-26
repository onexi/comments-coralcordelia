import openai
import sqlite3
import json
"""
Catagorizes comments into ethical (if a comment deals with ethical concerns), 
compliments the inteviewer / Sam Altman, talks about Altman personally, contains
hyperbolic language, or asks about the interview specifically.
"""
key = "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"
openai.api_key = key

con = sqlite3.connect('comments.db')
cur = con.cursor()
cur.execute("SELECT * FROM comments")
comments = cur.fetchmany(size = 1000)

combined_comments_and_responses = []

for (ind, comment) in enumerate(comments):
    if ind % 100 == 0:
        print(f'Processed {ind} comments so far.')
    try:
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
        cleaned_response = json.loads(response)
        assert isinstance(cleaned_response['ethical'], bool)
        assert isinstance(cleaned_response['compliment'], bool)
        assert isinstance(cleaned_response['personal'], bool)
        assert isinstance(cleaned_response['hyperbolic'], bool)
        assert isinstance(cleaned_response['interview'], bool)
        combined_comments_and_responses.append((cleaned_response, comment))
    except:
        print(f'ChatGPT gave invalid response on comment {ind}')

cur.execute("""
    ALTER TABLE comments
    ADD ethical INT
""")
cur.execute("""
    ALTER TABLE comments
    ADD compliment INT
""")
cur.execute("""
    ALTER TABLE comments
    ADD personal INT
""")
cur.execute("""
    ALTER TABLE comments
    ADD hyperbolic INT
""")
cur.execute("""
    ALTER TABLE comments
    ADD interview INT
""")

cur.executemany("""UPDATE comments
                SET (ethical, compliment, personal, hyperbolic, interview) = (?, ?, ?, ?, ?)
                WHERE cid = ?""", [(response['ethical'], response['compliment'], response['personal'], response['hyperbolic'], response['interview'], comment[0]) for (response, comment) in combined_comments_and_responses])

con.commit()