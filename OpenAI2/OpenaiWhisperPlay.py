# pip install openai, openai-whisper, ffmpeg-python
# That is fyi - however, do not do that. Rather, install from 
# within a Virtual Environment, using...
# [pip install -r requirements.txt]
# That is the easiest way to avoid some (perhaps Windows-specific)
# problems when installing the ffmpeg package - see below
# https://pypi.org/project/openai-whisper/
# rogue missing file:
# https://stackoverflow.com/questions/73845566/openai-whisper-filenotfounderror-winerror-2-the-system-cannot-find-the-file
# AttributeError: module 'ffmpeg' has no attribute 'input' or 'Error - probably due 
# to ffmpeg installation not ffmpeg-python on Windows
import whisper
from pathlib import Path 

class OpenAiWhisperPlay(object):
    
    def whisper_package_test(self, speech_file):
        currDir = Path().absolute()
        thefile = f"{currDir}\{speech_file}"
        print(thefile)
        model = whisper.load_model("small") # was base, medium (1.5GB)
        result = model.transcribe(thefile, verbose=True, fp16=False, language="en")

# Entry point
oap = OpenAiWhisperPlay()

audio_file = "short_tide.m4a"
#audio_file = "mahsound.mp3"

oap.whisper_package_test(audio_file)

