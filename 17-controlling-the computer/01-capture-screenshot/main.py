# we have to installl third party Library with this command : pip install mss
from mss import mss

with mss() as screen:
    screen.shot(output = '/Users/sepehr/Desktop/notes/PracticalLearningOfPython/17-controlling-the computer/01-capture-screenshot/screenshot.png')

