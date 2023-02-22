import time
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
x = 0.5
y= 0.2
time.sleep(2)
i=0;
mouse.position = (1650, 84)  #browse button
mouse.click(Button.left,1)
(1635, 99)
while i<10:
    time.sleep(y)
    mouse.position = (516,519) #browse button
    mouse.press(Button.left)
    time.sleep(x)
    mouse.release(Button.left)
    time.sleep(y)
    mouse.position = (515,552) #browse button
    mouse.press(Button.left)
    time.sleep(x)
    mouse.release(Button.left)
    
    i+=1
