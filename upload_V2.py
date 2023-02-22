import time
from pynput.mouse import Button, Controller
mouse = Controller()

from pynput.keyboard import Key, Controller
keyboard = Controller()

d = 1 #initial delay in seconds
N = 9 + 1 # the value 90 depends on the last name of the test pattern form drawing_v5



time.sleep(d)

i = 0
while i<N:
    mouse.position = (1556,570) #browse button
    mouse.click(Button.left, 1)
    time.sleep(0.5)


    keyboard.type("image"+str(i)+".png")
    time.sleep(0.5)
    keyboard.press(Key.enter)

    keyboard.release(Key.enter)
    time.sleep(0.5)

    mouse.position = (1656,605) # plus sign and repeat
    mouse.click(Button.left, 1)
    time.sleep(0.5)

    i+=1   # this value depends on the increment of the test pattern obtained from drawing_v5
