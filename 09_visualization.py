import plotly.express as px
import sqlite3
"""
Creates chart of relative frequencies of different characteristics of comments
"""
size_processed = 1000

con = sqlite3.connect('comments.db')
cur = con.cursor()
cur.execute("SELECT * FROM comments")
comments = cur.fetchmany(size = 1000)

counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
totals = [0, 0, 0, 0, 0, 0, 0, 0, 0]
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
    if comment[15] != None:
        totals[4] += 1
    if comment[15] == 1:
        counts[4] += 1
    if comment[16] != None:
        totals[5] += 1
    if comment[16] == 1:
        counts[5] += 1
    if comment[17] != None:
        totals[6] += 1
    if comment[17] == 1:
        counts[6] += 1
    if comment[18] != None:
        totals[7] += 1
    if comment[18] == 1:
        counts[7] += 1
    if comment[19] != None:
        totals[8] += 1
    if comment[19] == 1:
        counts[8] += 1


proportions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for ind, i in enumerate(counts):
    proportions[ind] = i / totals[ind]

fig = px.bar(x=["Negative", "Angry", "Spam", "Needs Response", "Ethical", "Compliment", "Personal", "Hyperbolic", "Interview"], y=proportions)
fig.update_xaxes(type='category') #since this is a catagorical graph
fig.show()
