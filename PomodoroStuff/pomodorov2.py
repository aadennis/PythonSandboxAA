# pip install pyttsx3
import pyttsx3
import datetime
import time

engine = pyttsx3.init()

while True:
    now = datetime.datetime.now()
    if now.minute % 15 == 0:
        hour_now = now.strftime("%H")
        engine.say(f"It is {hour_now} hundred hours")
        engine.runAndWait()
    time.sleep(60)
