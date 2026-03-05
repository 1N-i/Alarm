from playsound3 import playsound
from time import sleep
import os

os.system("") #Clears the terminal

#ANSI
CLEAR = "\033[2J" #Clears the terminal
HOME = "\033[H" #Goes back to the top
CLEAR_LINE = "\033[K" #Erases the rest of the text

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 #Get a integer number; 185 // 60 = 3
        seconds_left = time_left % 60 #Get what couldn't be divided; 185 % 60 = 5

        print(f"{HOME}{CLEAR_LINE}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    print("Times up!")
    playsound("alarm.mp3")

alarm(10) #10 seconds