# python scheduler
import schedule
import time
from playsound import playsound

def job():
    print("I am working...")
    playsound('sound(1).WAV') 

def play():
    print("Play Time...")
    playsound('sound(2).WAV') 
    
schedule.every(10).seconds.do(job) 
schedule.every(20).seconds.do(play) 

while True:  
    schedule.run_pending()  