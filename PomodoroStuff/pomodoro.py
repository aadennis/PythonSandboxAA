# pip install win10toast
from win10toast import ToastNotifier
import datetime
import time

toaster = ToastNotifier()

while True:
    now = datetime.datetime.now()
    if now.minute % 20 == 0:
        hour_now = now.strftime("%H")
        toaster.show_toast("Announcing Time", f"It is {hour_now} o'clock", duration=10)
    time.sleep(60)
