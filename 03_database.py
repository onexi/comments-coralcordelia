import sqlite3
import json

def open_file(file):
    with open(file, 'r') as infile:
        output = json.loads(infile.read())
        return output

comments = open_file('comments.json')['comments']
con = sqlite3.connect("comments.db")
cur = con.cursor()

# Create the table
cur.execute('''CREATE TABLE IF NOT EXISTS comments
             (cid TEXT,
              text TEXT,
              time TEXT,
              author TEXT,
              channel TEXT,
              votes TEXT,
              photo TEXT,
              heart INTEGER,
              reply INTEGER,
              time_parsed DECMIAL,
              negative INTEGER,
              angry INTEGER,
              spam INTEGER,
              response TEXT)''')

# Insert data into the table
rows_to_insert = [(comment['cid'], comment['text'], comment['time'], 
    comment['author'], comment['channel'], comment['votes'], 
    comment['photo'], int(comment['heart']), int(comment['reply']), 
    comment['time_parsed']) for comment in comments]


cur.executemany('''INSERT OR IGNORE INTO comments(cid, text, time, author, channel, votes, photo, heart, reply, time_parsed) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', rows_to_insert)
con.commit()