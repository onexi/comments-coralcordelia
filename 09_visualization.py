import plotly.express as px
import sqlite3

size_processed = 1000

con = sqlite3.connect('comments.db')
cur = con.cursor()
cur.execute("SELECT * FROM comments")
comments = cur.fetchmany(size = 1000)

counts = [0, 0, 0, 0]
totals = [0, 0, 0, 0]
for comment in comments:
    if comment[10] != None:
        totals[0] += 1
    if comment[10] == 1:
        counts[0] += 1
    if comment[11] != None:
        totals[1] += 1
    if comment[11] == 1:
        counts[1] += 1
    if comment[12] != None:
        totals[2] += 1
    if comment[12] == 1:
        counts[2] += 1
    if comment[13] != None:
        totals[3] += 1
    if comment[13] == 1:
        counts[3] += 1


proportions = [0, 0, 0, 0]
for ind, i in enumerate(counts):
    proportions[ind] = i / totals[ind]

fig = px.bar(x=["Negative", "Angry", "Spam", "Needs Response"], y=proportions)
fig.update_xaxes(type='category') #since this is a catagorical graph
fig.show()
