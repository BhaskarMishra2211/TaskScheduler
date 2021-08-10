import winsound
from win10toast import ToastNotifier

def timer(reminder,seconds):
    notificator = ToastNotifier()
    notificator.show_toast(f"Reminder",reminder,duration = 20)

    winsound.PlaySound('sound(1).wav', winsound.SND_FILENAME) 

t = timer("Play Time",20)
print(t)