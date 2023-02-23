from pynput.mouse import Button, Controller
from screeninfo import get_monitors
import os 

monitors = get_monitors();

mouse = Controller()
ww = monitors[0].width 
hh = monitors[0].height

run = True
while run:
    x = mouse.position[0]
    y = mouse.position[1]
    if x < ww - ww / 3 or y < hh - hh / 3:
        os.system('pmset displaysleepnow')
        run = False
