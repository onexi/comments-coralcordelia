import sqlite3

con = sqlite3.connect('comments.db')
cur = con.cursor()
cur.execute("SELECT * FROM comments")
comments = cur.fetchmany(size = 26)[1:]

properties = [
    {'angry': False, 'negative': True, 'response': True, 'spam': False},
    {'angry': False, 'negative': True, 'response': False, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': True},
    {'angry': False, 'negative': False, 'response': False, 'spam': True},
    {'angry': False, 'negative': False, 'response': False, 'spam': True},
    {'angry': False, 'negative': False, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': True, 'spam': False},
    {'angry': False, 'negative': True, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': False},
    {'angry': False, 'negative': True, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': False},
    {'angry': False, 'negative': True, 'response': True, 'spam': False},
    {'angry': False, 'negative': True, 'response': False, 'spam': False},
    {'angry': False, 'negative': True, 'response': False, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': False},
    {'angry': False, 'negative': False, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': False}
]

for ind, comment in enumerate(comments):
    print(f'Comment {ind}: {comment[1]}\nDictionary: {properties[ind]}')