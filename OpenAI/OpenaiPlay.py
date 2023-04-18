# pip install openai openai-whisper
# choco install ffmpeg
# playing - chat.openai.com/chat
# https://pypi.org/project/openai/
import openai
import os
import util
import whisper

class OpenAiPlay(object):
    def __init__(self):
        # This assumes you have pasted the api key into your clipboard before
        # execution
        self.api_key = util.get_clipboard()
       
    def davinci_test(self): 
        # alternative ways to get the key
        #key = getpass.getpass('Enter the api key:') # import getpass
        #key = open('key.txt').read().strip('\n')
        openai.api_key = self.api_key
        prompt = "Write an advertising slogan for a soft drink"
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            temperature=0.8, # high temp = high randomness
            max_tokens=1000 # you pay per 1k token - input and output
        )
        print(response)
        # print(response['choices'][0]['message']['content'])

    # https://platform.openai.com/docs/guides/speech-to-text/quickstart
    # https://platform.openai.com/docs/guides/speech-to-text/prompting
    def whisper_test(self, speech_file):
        openai.api_key = self.api_key
        with open(speech_file, 'rb') as audio_file:
            transcript = openai.Audio.transcribe(file=audio_file, model='whisper-1', prompt='High\nLow')
            print(transcript)

    def whisper_api_test(self, speech_file):
        model = whisper.load_model("base")
        result = model.transcribe(speech_file)
        print(result["text"])



oap = OpenAiPlay()

#oap.davinci_test()

# The passed speech file can be found in 
# OD\data\photos\2023\2023_03\GoogleSpeech\definitive_test_input.mp3
# Put a working copy in this OpenAI folder - mark as Ignore, as too big for GitHub
audio_file = "OpenAI/test_artefacts/definitive_test_input.mp3"
audio_file = "OpenAI/test_artefacts/short_tide.m4a"

# oap.whisper_test(audio_file)
oap.whisper_api_test(audio_file)

