# pip install openai
# playing - chat.openai.com/chat
# https://pypi.org/project/openai/

import openai
import util

# alternative ways to get the key
#key = getpass.getpass('Enter the api key:') # import getpass
#key = open('key.txt').read().strip('\n')

openai.api_key = util.get_clipboard()
prompt = "Write an advertising slogan for a soft drink"
response = openai.Completion.create(
    model='text-davinci-003',
    prompt=prompt,
    temperature=0.8, # high temp = high randomness
    max_tokens=1000 # you pay per 1k token - input and output
)
print(response)
# print(response['choices'][0]['message']['content'])

