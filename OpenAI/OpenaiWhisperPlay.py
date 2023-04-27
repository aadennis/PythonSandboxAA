# pip install openai, openai-whisper, ffmpeg-python
# https://pypi.org/project/openai-whisper/
# rogue missing file:
# https://stackoverflow.com/questions/73845566/openai-whisper-filenotfounderror-winerror-2-the-system-cannot-find-the-file
# AttributeError: module 'ffmpeg' has no attribute 'input' or 'Error - probably due 
# to ffmpeg installation not ffmpeg-python
# on Windows
import whisper
from pathlib import Path 

class OpenAiWhisperPlay(object):
    
    def whisper_package_test(self, speech_file):
        print("File Path:", Path(__file__).absolute()) 
        print("Directory Path:", Path().absolute()) # Directory of current working directory, not __file__
        currDir = Path().absolute()
        thefile = f"{currDir}\{speech_file}"
        print(thefile)

        model = whisper.load_model("base")
        result = model.transcribe(thefile, verbose=True, fp16=False, language="en")


oap = OpenAiWhisperPlay()

audio_file = "OpenAI/test_artefacts/short_tide.m4a"
audio_file = "mahsound.mp3"

# oap.whisper_test(audio_file)
oap.whisper_package_test(audio_file)

