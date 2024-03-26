import os
"""
Runs each of the programs sequentially
"""
os.system('python setup_requirements.py')

print('01: Extracting comments...')
os.system('python 01_extract.py')
print('02: Counting comments...')
os.system('python 02_count.py')
print('03: Creating database...')
os.system('python 03_database.py')
print('05: Pinging OpenAI...')
os.system('python 05_ping_openai.py')
print('06: Catagorizing data based on type...')
os.system('python 06_prediction.py')
print('07: Generating responses to comments...')
os.system('python 07_create_responses.py')
print('08: Catagorizing comments some more...')
os.system('python 08_catagories.py')
print('10: Generating clean dataset...')
os.system('python 10_clean_dataset.py')

print('09: Generating visualization... Press Ctrl + C and run 09_visualization.py if visualization does not show.')
os.system('python 09_visualization.py')