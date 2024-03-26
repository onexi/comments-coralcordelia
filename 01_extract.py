"""
01: We simply take the comments straight from the video to clean_dataset by calling the terminal. This is useful for using terminal-only features, like limiting comment count.
"""

# from itertools import islice
# import json
# from youtube_comment_downloader import *
# downloader = YoutubeCommentDownloader()
# comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=L_Guz73e6fw', sort_by=SORT_BY_RECENT)
# most_recent_comments = list(islice(comments, 100))
# with open('comments.json', 'w') as outfile:
#     json.dump(most_recent_comments, outfile, ensure_ascii=False, indent=4)

import os

os.system("""youtube-comment-downloader --url https://www.youtube.com/watch?v=L_Guz73e6fw --sort 1 --output comments.json --pretty""")
# lmao absolutely ingenius strategy
