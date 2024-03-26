import openai
import sqlite3
"""
Generating responses to select comments
"""

key = "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"
openai.api_key = key

con = sqlite3.connect('comments.db')
cur = con.cursor()
cur.execute("SELECT * FROM comments")
comments = cur.fetchmany(size = 1000)

combined_comments_and_responses = []

for ind, comment in enumerate(comments):
    if ind % 100 == 0:
        print(f'Processed {ind} comments so far.')
    if comment[13] == 1 or comment[13] == '1':
        try:
            message_to_send_to_ai = {
                "role": "user",
                "content": f"""I have a comment on a video about Sam Altman's interview concerning ChatGPT-4. 
                Please write a response to this comment. If the comment expresses concerns towards the interview, Sam Altman, 
                OpenAI, or AI in general, make sure you address the user and acknowledge their concerns,
                but that you ultimately accurately respond to criticism about Sam Altman and the interview. To comments speaking
                complimenting the interview, be sure to thank the user. Remember to keep the comment brief. Put only the text you would write in the comment (Do not write "Response:" or "Comment:" at the beginning of the comment.) Here is the comment, typed by {comment[3]}: {comment[1]}.
                """
            }
            message = openai.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = [message_to_send_to_ai])
            response = message.choices[0].message.content.strip()
            combined_comments_and_responses.append((str(response), comment))
        except:
            print(f'ChatGPT gave invalid response on comment {ind}')

cur.execute("""
    ALTER TABLE comments
    ADD responses TEXT;
""")

cur.executemany("""UPDATE comments
                SET (responses) = (?)
                WHERE cid = ?""", [(response, comment[0]) for (response, comment) in combined_comments_and_responses])


con.commit()