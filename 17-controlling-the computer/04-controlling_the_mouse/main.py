# in this section we will learn how to controll the mouse.
# for this section we will need to pip install the library called pyautogui
import pyautogui
# this cide will show us the current posiotion of the mouse (the coordinate of the mouse and the (0,0) is at the top left side of the screen): 
positions = pyautogui.position()
print(positions) # we need this coordinates to move the  ouse up to the places that we want our program click and do some works for us.
# I have mannually changed the keybord short cuts by command k s keys and set command + p to run python file so I would't have to move the mouse where I don't want the coordinates.

# to move th ecursor we use moveto method:
pyautogui.moveTo(125,855,1) # and we can make the proccess more natural by seting the next parameter as duration and give the inputs as seconds

# if you would want to click that item you would apply the click method:
pyautogui.click(clicks=2) # if you need a double click you put clicks parameter to 2
# also we could not use the move to methos ==d and giev the coordinates to the click method, and then that will do the work for us.
# if we want to perform a right click we use the same process but slightly diffrent this time:
pyautogui.click(button='right') # by default the value id left.

# we can also move the cursor by using move method:

pyautogui.move(500,10,duration=1)