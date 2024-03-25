import os

os.system('python setup_requirements.py')

print('Extracting comments...')
os.system('python 01_extract.py')
print('Counting comments...')
os.system('python 02_count.py')
print('Creating database...')
os.system('python 03_database.py')
print('Pinging OpenAI...')
os.system('python 05_ping_openai.py')
print('Catagorizing data based on type...')
os.system('python 06_prediction.py')
print('Generating responses to comments...')
os.system('python 07_create_responses.py')
print('Catagorizing comments some more...')
os.system('python 08_catagories.py')
print('Generating clean dataset...')
os.system('python 10_clean_dataset.py')

print('Generating visualization...')
os.system('python 09_visualization.py')