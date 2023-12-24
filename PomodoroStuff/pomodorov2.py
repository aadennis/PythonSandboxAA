# pip install pyttsx3
import pyttsx3
import datetime
import time

def announce_time(now_time = datetime.datetime.now()):
    engine = pyttsx3.init()

    while True:
        now = now_time
        if now.minute % 15 == 0:
            hour_now = int(now.strftime("%H"))
            am_pm = now.strftime("%p")
            minutes = ""
            if am_pm == 'PM':
                hour_now = hour_now - 12
            else: # engine cannot pronounce 'AM'
                am_pm = "eh em"
            if now.minute > 0:
                minutes = str(now.minute)
            engine.say(f"It is {hour_now} {minutes} {am_pm}")
            engine.runAndWait()
        time.sleep(60)

if __name__ == "__main__":
    year=2023
    month=11
    day=30
    hour=14
    minute=0
    #minute=15
    #minute=30
    #minute=45
    

    now = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute)
    announce_time(now)

