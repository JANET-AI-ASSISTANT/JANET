from datetime import datetime
from threading import Timer
from audio.tts import say
now = datetime.now()
time = now.time()
def tell_time():
    say("the time is "+ str(time))

def end_timer():
    say("Timer finished!")

def set_timer():
    t = Timer(10.0, end_timer)
    t.start()

