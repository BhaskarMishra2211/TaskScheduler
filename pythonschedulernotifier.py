import schedule # install schedule 
import time
from playsound import playsound # install playsound 

# list of task
def wakeup():
    print("Wakeup Wakeup...")
    playsound("sound(1).wav")

schedule.every(5).seconds.do(wakeup)

def officetime():
    print("Ofiice time")
    playsound("sound(2).wav")

schedule.every(2).seconds.do(officetime)

def dinnertime():
    print("Dinner time")
    playsound("sound(3).wav")

schedule.every().day.at("17:37").do(dinnertime)

def movieremainder():
    print("Today you have to watch the movie")
    playsound("reminder.mp3")

schedule.every().day.at("17:38").do(movieremainder)

while True:
    schedule.run_pending()
    time.sleep(10)