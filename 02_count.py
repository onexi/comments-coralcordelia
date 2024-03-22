"""
02: Count the comments!
"""
import json

def open_file(file):
    with open(file, 'r') as infile:
        output = json.loads(infile.read())
        return output

comments = open_file('comments.json')
print(f'Number of comments loaded: {len(comments["comments"])}')