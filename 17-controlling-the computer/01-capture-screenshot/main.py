# we have to installl third party Library with this command : pip install mss
from mss import mss
from datetime import datetime as dt
import time
import keyboard

def take_screen_shot():
    dir = '/Users/sepehr/Desktop/notes/PracticalLearningOfPython/17-controlling-the computer/01-capture-screenshot'
    while True:
        file_name = '/'+ str(dt.now())+'.png'
        with mss() as screen:
            screen.shot(output=dir+file_name)
            if keyboard.is_pressed(ord('q')):
                break
        time.sleep(600)
        


def main():
    take_screen_shot()
        

main()


