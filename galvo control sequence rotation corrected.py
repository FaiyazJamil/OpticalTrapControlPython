
#keep the remote window size 75% on the other computer
import time
from pynput.mouse import Button, Controller
mouse = Controller()

from pynput.keyboard import Key, Controller
keyboard = Controller()


N = int(input('Set speed: 1-10:  \n1 is the fastest speed\n10 is the slowest speed'))/10
input("Press Enter to continue...")
global x
global y
global angle
global scale
x=0.0
y=0.0
angle=0
scale=100
align_x=1876 #align button coordinate
align_y=343
OffX_x= 1210 #OffX button coordinate
OffX_y= 362
OffY_x= 1210 #OffY button coordinate
OffY_y= 382
ScaleX_x = 1210 #ScaleX button coordinate
ScaleX_y = 415
ScaleY_x = 1210 #ScaleY button coordinate
ScaleY_y = 435
Angle_x = 1210 #Angle button coordinate
Angle_y = 473
OK_x = 1166
OK_y = 506


user_input = input('Please input the order in which you want to manipulate separated by a space:\n U-up \n D-down \n L-left \n R-right \n CW-Clockwise rotation \n CCW-CounterClockwise Rotation \n SxU-Scale up along x-axis \n SxD-Scale down along x-axis \n SyU-Scale up along y-axis \n SyD-Scale down along y-axis \n de-default settings  :  ')
split = user_input.split()

list = ["U","D","L","R","CW","CCW","SxU","SxD","SyD","SyU","de"]




def de():
        mouse.position = (align_x,align_y) #align button
        mouse.click(Button.left, 1)
        time.sleep(0.05)
        

        mouse.position = (OffX_x,OffX_y) # OFFset X
        mouse.click(Button.left, 2)
        time.sleep(0.5)
        keyboard.type(str(0))
        mouse.position = (OffY_x,OffY_y) # OFFset Y
        mouse.click(Button.left, 2)
        time.sleep(0.5)
        keyboard.type(str(0))
        mouse.position = (ScaleX_x,ScaleX_y) # Scale X
        mouse.click(Button.left, 2)
        time.sleep(0.5)
        keyboard.type(str(scale))
        mouse.position = (ScaleY_x,ScaleY_y) # Scale Y
        mouse.click(Button.left, 2)
        time.sleep(0.5)
        keyboard.type(str(scale))
        mouse.position = (Angle_x,Angle_y) # Angle
        mouse.click(Button.left, 2)
        time.sleep(0.5)
        keyboard.type(str(0))
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)


def U():
        
        global x
        global y
        global angle
        global scale
        i=0
        x1=x
        while i<10:             # a 10 step process
            mouse.position = (align_x,align_y) #align button
            mouse.click(Button.left, 1)
            time.sleep(0.01)


            mouse.position = (OffX_x,OffX_y)
            mouse.click(Button.left, 1)
            keyboard.press(Key.shift)
            keyboard.press(Key.home)
           
            keyboard.release(Key.home)
            keyboard.release(Key.shift)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)

            keyboard.type(str(x1))
            time.sleep(0.01)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
           
            time.sleep(N)

            
            x1 = round((x+float("0."+str(i))),2)
            i+=1
            # this value depends on the increment of the test pattern obtained from drawing_v5
       
        x= x1
        


def D():
        global x
        global y
        global angle
        global scale
        i=0
        x1=x
        while i<10:             # a 10 step process
            mouse.position = (align_x,align_y) #align button
            mouse.click(Button.left, 1)
            time.sleep(0.01)


            mouse.position = (OffX_x,OffX_y)
            mouse.click(Button.left, 1)
            keyboard.press(Key.shift)
            keyboard.press(Key.home)
           
            keyboard.release(Key.home)
            keyboard.release(Key.shift)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)

            keyboard.type(str(x1))
            time.sleep(0.01)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
           
            time.sleep(N)

            
            x1 = round((x-float("0."+str(i))),2)
               # this value depends on the increment of the test pattern obtained from drawing_v5
            ###
            i+=1
        x= x1


def R():
        global x
        global y
        global angle
        global scale
        i = 0
        y1=y
        while i<10:             # a 10 step process
            mouse.position = (align_x,align_y) #align button
            mouse.click(Button.left, 1)
            time.sleep(0.05)


            mouse.position = (OffY_x,OffY_y)
            mouse.click(Button.left, 1)
            keyboard.press(Key.shift)
            keyboard.press(Key.home)
           
            keyboard.release(Key.home)
            keyboard.release(Key.shift)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
            keyboard.type(str(y1))
            time.sleep(0.05)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
           
            time.sleep(N)


            y1 = round((y+float("0."+str(i))),2)
            i+=1   # this value depends on the increment of the test pattern obtained from drawing_v5
            ###
        y= y1

      
def L():
        global x
        global y
        global angle
        global scale
        i = 0
        y1=y
        while i<10:             # a 10 step process
            mouse.position = (align_x,align_y) #align button
            mouse.click(Button.left, 1)
            time.sleep(0.05)

            mouse.position = (OffY_x,OffY_y)
            mouse.click(Button.left, 1)
            keyboard.press(Key.shift)
            keyboard.press(Key.home)
           
            keyboard.release(Key.home)
            keyboard.release(Key.shift)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
            keyboard.type(str(y1))
            time.sleep(0.05)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
           
            time.sleep(N)


            y1 = round((y-float("0."+str(i))),2)
            i+=1   # this value depends on the increment of the test pattern obtained from drawing_v5
            ###
        y= y1

      
    
def CW():
        global x
        global y
        global angle
        global scale
        i = 0
        res = 5
        angle_limit = 45
        angle1=angle

        while i < angle_limit+1:             # a 10 step process
            mouse.position = (align_x,align_y) #align button
            mouse.click(Button.left, 1)
            time.sleep(0.05)


            mouse.position = (Angle_x,Angle_y)
            mouse.click(Button.left, 1)
            keyboard.press(Key.shift)
            keyboard.press(Key.home)
           
            keyboard.release(Key.home)
            keyboard.release(Key.shift)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)

            keyboard.type(str(angle1))
            time.sleep(0.05)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
           
            time.sleep(N)


            angle1 = angle+float(str(i))
            i= i+ float(res)  # this value depends on the increment of the test pattern obtained from drawing_v5
            ###
        angle= angle1
        

def CCW():
        global x
        global y
        global angle
        global scale
        i = 0
        res = 5
        angle_limit = 45
        angle1=angle
        while i<angle_limit+1:             # a 10 step process
            mouse.position = (align_x,align_y) #align button
            mouse.click(Button.left, 1)
            time.sleep(0.05)


            mouse.position = (Angle_x,Angle_y)
            mouse.click(Button.left, 1)
            keyboard.press(Key.shift)
            keyboard.press(Key.home)
           
            keyboard.release(Key.home)
            keyboard.release(Key.shift)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)

            keyboard.type(str(angle1))
            time.sleep(0.05)

            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
           
            time.sleep(N)


            angle1 = angle-float(str(i))
            i= i+ float(res)   # this value depends on the increment of the test pattern obtained from drawing_v5
            ###
        angle= angle1


def SxU():
        global x
        global y
        global angle
        global scale
        i = 0
        res = 5
        scale_limit = 1.5
        scale1=scale
        while i<100*(scale_limit-1):             # a 10 step process
            mouse.position = (align_x,align_y) #align button
            mouse.click(Button.left, 1)
            time.sleep(0.05)


            mouse.position = (ScaleX_x,ScaleX_y)
            mouse.click(Button.left, 1)
            keyboard.press(Key.shift)
            keyboard.press(Key.home)
           
            keyboard.release(Key.home)
            keyboard.release(Key.shift)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)

            keyboard.type(str(scale1))
            time.sleep(0.05)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
           
            time.sleep(N)


            scale1 = scale+float(str(i))
            i= i+ float(res)  # this value depends on the increment of the test pattern obtained from drawing_v5
            ###


        scale= scale1


def SxD():
        global x
        global y
        global angle
        global scale
        i = 0
        res = 5
        scale_limit = 1.5
        scale1=scale
        while i<100*(scale_limit-1):             # a 10 step process
            mouse.position = (align_x,align_y) #align button
            mouse.click(Button.left, 1)
            time.sleep(0.05)


            mouse.position = (ScaleX_x,ScaleX_y)
            mouse.click(Button.left, 1)
            keyboard.press(Key.shift)
            keyboard.press(Key.home)
           
            keyboard.release(Key.home)
            keyboard.release(Key.shift)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)

            keyboard.type(str(scale1))
            time.sleep(0.05)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
           
            time.sleep(N)


            scale1 = scale-float(str(i))
            i= i+ float(res)  # this value depends on the increment of the test pattern obtained from drawing_v5
            ###

        scale= scale1
       

def SyU():
        global x
        global y
        global angle
        global scale
        i = 0
        res = 5
        scale_limit = 1.5
        scale1=scale
        while i<100*(scale_limit-1):             # a 10 step process
            mouse.position = (align_x,align_y) #align button
            mouse.click(Button.left, 1)
            time.sleep(0.05)


            mouse.position = (ScaleY_x,ScaleY_y)
            mouse.click(Button.left, 1)
            keyboard.press(Key.shift)
            keyboard.press(Key.home)
           
            keyboard.release(Key.home)
            keyboard.release(Key.shift)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)

            keyboard.type(str(scale1))
            time.sleep(0.05)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
           
            time.sleep(N)


            scale1 = scale+float(str(i))
            i= i+ float(res)  # this value depends on the increment of the test pattern obtained from drawing_v5
            ###

        scale= scale1
 
def SyD():
        global x
        global y
        global angle
        global scale
        i = 0
        res = 5
        scale_limit = 1.5
        scale1=scale
        while i<100*(scale_limit-1):             # a 10 step process
            mouse.position = (align_x,align_y) #align button
            mouse.click(Button.left, 1)
            time.sleep(0.05)


            mouse.position = (ScaleY_x,ScaleY_y)
            mouse.click(Button.left, 1)
            keyboard.press(Key.shift)
            keyboard.press(Key.home)
           
            keyboard.release(Key.home)
            keyboard.release(Key.shift)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)

            keyboard.type(str(scale1))
            time.sleep(0.05)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
           
            time.sleep(N)


            scale1 = scale-float(str(i))
            i= i+ float(res)  # this value depends on the increment of the test pattern obtained from drawing_v5
            ###

        scale= scale1

p=0
while p<len(split):
    if split[p] in list:
        eval(split[p])()
    else:
        print(split[p]+' does not exist as a command')
    p+=1