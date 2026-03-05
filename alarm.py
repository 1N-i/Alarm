#https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203
from playsound3 import playsound
import time

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 #Get a integer number; 185 // 60 = 3
        seconds_left = time_left % 60 #Get what couldn't be divided; 185 % 60 = 5

        print(f"{minutes_left}:{seconds_left}")
    playsound("alarm.mp3")

alarm(10)