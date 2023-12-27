# Speak the time every 15 minutes.
# Most of the effort is around achieving a natural-sounding 
# phrase for each point in the day.
# Testing: this is done by passing announce_time the datetime
# under test. If no argument is passed, then the function
# uses the clock time. 
# Example call: python  announce_time()

# pip install pyttsx3
import pyttsx3
import datetime
import time

def get_time(args):
    has_argument = bool(len(args))
    if has_argument:
        return args[0]
    return datetime.datetime.now()

def announce_time(*args):
    
    engine = pyttsx3.init()
    engine.setProperty('volume', 0.5)

    while True:
        now = get_time(args)
        if now.minute % 15 == 0:
            hour_now = int(now.strftime("%H"))
            am_pm = now.strftime("%p")
            minutes = ""
            if am_pm == 'PM':
                hour_now = hour_now - 12
            else: # engine cannot pronounce 'AM'
                am_pm = "A M"
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
    

    # test values...
    # now_time = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute)
    # announce_time(now_time)

    # "production" run...
    announce_time()

