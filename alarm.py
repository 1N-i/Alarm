from playsound3 import playsound
import time

#ANSI
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 #Get a integer number; 185 // 60 = 3
        seconds_left = time_left % 60 #Get what couldn't be divided; 185 % 60 = 5

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm.mp3")

alarm(10)