# pip install pyttsx3
import pyttsx3
import datetime
import time

def announce_time():
    engine = pyttsx3.init()

    while True:
        now = datetime.datetime.now()
        if now.minute % 15 == 0:
            hour_now = now.strftime("%H")
            engine.say(f"It is {hour_now} o'clock")
            engine.runAndWait()
        time.sleep(60)

if __name__ == "__main__":
    announce_time()

