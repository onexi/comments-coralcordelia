import sqlite3
import json

con = sqlite3.connect('comments.db')
cur = con.cursor()
cur.execute("SELECT * FROM comments")
comments = cur.fetchmany(size = 26)[1:]

properties = [
    {'angry': True, 'negative': True, 'response': False, 'spam': False},
    {'angry': False, 'negative': True, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': True},
    {'angry': True, 'negative': True, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': True, 'spam': False},
    {'angry': False, 'negative': True, 'response': True, 'spam': False},
    {'angry': False, 'negative': True, 'response': False, 'spam': False},
    {'angry': False, 'negative': False, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': True},
    {'angry': False, 'negative': False, 'response': True, 'spam': False},
    {'angry': False, 'negative': True, 'response': True, 'spam': False},
    {'angry': False, 'negative': True, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': True, 'spam': False},
    {'angry': False, 'negative': True, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': True},
    {'angry': False, 'negative': False, 'response': False, 'spam': True},
    {'angry': False, 'negative': False, 'response': False, 'spam': True},
    {'angry': False, 'negative': False, 'response': True, 'spam': False},
    {'angry': False, 'negative': True, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': True},
    {'angry': False, 'negative': False, 'response': False, 'spam': False},
    {'angry': False, 'negative': True, 'response': True, 'spam': False},
    {'angry': False, 'negative': False, 'response': False, 'spam': True},
    {'angry': False, 'negative': False, 'response': False, 'spam': True},
    {'angry': False, 'negative': False, 'response': False, 'spam': True} 
]

with open('sample_data.json', 'w') as outfile:
    outfile.dump(properties)

for ind, comment in enumerate(comments):
    print(f'Comment {ind}: {comment[1]}\nDictionary: {properties[ind]}')