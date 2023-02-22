#keep the remote window size 75% on the other computer
import time
from pynput.mouse import Button, Controller
mouse = Controller()

from pynput.keyboard import Key, Controller
keyboard = Controller()


N = int(input('Set speed: 1-10:  \n1 is the fastest speed\n10 is the slowest speed'))/10
input("Press Enter to continue...")
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

def move():

    global x
    global y
    global angle
    global scale
    user_input = input('Please Select: U/D/L/R/CW/CCW/SxUP/SxDW/SyUP/SyDW/def :  ')


    if user_input == 'def':
        
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



    if user_input == 'U':
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
        move()


    if user_input == 'D':
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
        move()

    if user_input == 'R':
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
        move()
      
    if user_input == 'L':
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
        move()
      
    
    if user_input == 'CW':
        i = 0
        res = input('Insert angle resolution: ')
        angle_limit = float(input('Insert the angle limit'))
        angle1=angle

        while i < angle_limit:             # a 10 step process
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
        move()

    if user_input == 'CCW':
        i = 0
        res = input('Insert angle resolution: ')
        angle_limit = float(input('Insert the angle limit'))
        angle1=angle
        while i<angle_limit:             # a 10 step process
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
        move()

    if user_input == 'SxUP':
        i = 0
        res = input('Insert scale resolution: ')
        scale_limit = float(input('Insert scale limit: (for 2x up scale insert 2) '))
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
        move()

    if user_input == 'SxDW':
        i = 0
        res = input('Insert scale resolution: ')
        scale_limit = float(input('Insert scale limit: (for 2x down scale insert 2) '))
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
        move()
    if user_input == 'SyUP':
        i = 0
        res = input('Insert scale resolution: ')
        scale_limit = float(input('Insert scale limit: (for 2x down scale insert 2) '))
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
        move()
    if user_input == 'SyDW':
        i = 0
        res = input('Insert scale resolution: ')
        scale_limit = float(input('Insert scale limit: (for 2x down scale insert 2) '))
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
        move()

move()