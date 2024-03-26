import sqlite3
import json
"""
Exports clean JSON file of the comments
"""
con = sqlite3.connect('comments.db')
cur = con.cursor()
cur.execute("SELECT * FROM comments")
comments = cur.fetchall()

clean_dataset = [
    {
        "cid": comment[0],
        "comment": comment[1],
        "user": comment[2],
        "author": comment[3],
        "channel": comment[4],
        "votes": comment[5],
        "photo": comment[6],
        "heart": comment[7],
        "reply": comment[8],
        "time_parsed": comment[9],
        "negative": comment[10],
        "angry": comment[11],
        "spam": comment[12],
        "response": comment[13],
        "ai response": comment[14],
        "ethical": comment[15],
        "compliment": comment[16],
        "personal": comment[17],
        "hyperbolic": comment[18],
        "interview": comment[19]
    }
    for comment in comments]

with open('clean_dataset.json', 'w') as outfile:
    json.dump(clean_dataset, outfile, ensure_ascii=False, indent=4)
    print('Clean dataset saved to : clean_dataset.json')