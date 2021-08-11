import schedule
import time
from playsound import playsound

# some task
def wakeupcall():
    print("Wakeup Wakeup")
    playsound("sound(1).WAV")

schedule.every(10).seconds.do(wakeupcall)

def officetime():
    print("Office time...")
    playsound("reminder.mp3")

schedule.every().day.at("12:17").do(officetime)

def movieremainder():
    print("Movie Time...")
    playsound("Reminder (1).mp3")

schedule.every().day.at("12:18").do(movieremainder)


while True:
    schedule.run_pending()
    time.sleep(10)