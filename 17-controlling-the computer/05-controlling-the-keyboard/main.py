# in this section we will learn how to controll Keyboard using python , we will use pyautogui Library

import pyautogui
import time
# the first action is to double click on the sample.txt file


pyautogui.doubleClick(142,860)
# and now we need to use keyboard.
# we use press method and put in as paramtere 'down'
time.sleep(1)
pyautogui.press('down')
# now we press Enter key:
pyautogui.press('enter')
pyautogui.write('Hello')
