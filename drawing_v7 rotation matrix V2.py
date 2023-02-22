import time
from PIL import Image, ImageDraw, ImageFont
import math
from pynput.keyboard import Key, Controller
keyboard = Controller()
from scipy.optimize import fsolve
import numpy as np
from pynput.mouse import Button, Controller
mouse = Controller()



canvas = (1920, 1200) #resolution of the SLM

Dir = r'C:\Users\mjamil\OneDrive - University of Massachusetts Dartmouth\Python Control\Test Patterns'
# im = Image.new('RGBA', canvas, (255, 255, 255, 255))
# draw = ImageDraw.Draw(im)
#declaring the initial position of the tra[p]
x = 960
y = 600
#r = input('Insert the radius:')
r=240
x1=r
y1=0
x2=-r
y2=0
x3=0
y3=r
x4=0
y4=-r
theta = 0
rt = 0
i=0 #this is not required

Trp_size = 30
res = 15 # resolution of the movement of the traps



def move():

    user =  input('Which way?')
    global x
    global y
    global x1
    global y1
    global x2
    global y2
    global x3
    global y3
    global x4
    global y4
    global theta
    global rt


    if user == 'right':
        i=0
        j=0
        while i < res*10:
            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)

            if i == 0:
                sin = np.sin(int(theta)*3.1416/180)
                cos = np.cos(int(theta)*3.1416/180)
            elif i == res:
                sin = np.sin(-int(theta)*3.1416/180)
                cos = np.cos(-int(theta)*3.1416/180)

            x1=r+i
            y1=0
            x2=-r+i
            y2=0
            x3=i
            y3=r
            x4=i
            y4=-r

            sin = np.sin(int(theta)*3.1416/180)
            cos = np.cos(int(theta)*3.1416/180)

            a = np.array([[x1],[y1]])
            b = np.array([[x2],[y2]])
            c = np.array([[x3],[y3]])
            d = np.array([[x4],[y4]])

            R = np.array([[cos, -sin],
                [sin, cos]])

            d1 = np.array([[x],[y]])

            A = np.dot(R,a)+d1
            B = np.dot(R,b)+d1
            C = np.dot(R,c)+d1
            D = np.dot(R,d)+d1

            x1 = A[0,0]
            y1 = A[1,0]
            x2 = B[0,0]
            y2 = B[1,0]
            x3 = C[0,0]
            y3 = C[1,0]
            x4 = D[0,0]
            y4 = D[1,0]


            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x2,y2, x2+Trp_size,y2+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x3,y3, x3+Trp_size,y3+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x4,y4, x4+Trp_size,y4+Trp_size), fill = (0,0,0), width = 0)
            im.save(Dir+'/Image'+str(j)+'.png')

            i +=res
            j+=1

        exec(open("upload_V2.py").read())
        x = x1-r #saving the previous coordinates
        y = y1
        move()

    if user == 'left':
        i=0
        j=0
        while i < res*10:
            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)
            if i == 0:
                sin = np.sin(int(theta)*3.1416/180)
                cos = np.cos(int(theta)*3.1416/180)
            elif i == res:
                sin = np.sin(-int(theta)*3.1416/180)
                cos = np.cos(-int(theta)*3.1416/180)

            x1=r-i
            y1=0
            x2=-r-i
            y2=0
            x3=-i
            y3=r
            x4=-i
            y4=-r

            sin = np.sin(int(theta)*3.1416/180)
            cos = np.cos(int(theta)*3.1416/180)

            a = np.array([[x1],[y1]])
            b = np.array([[x2],[y2]])
            c = np.array([[x3],[y3]])
            d = np.array([[x4],[y4]])

            R = np.array([[cos, -sin],
                [sin, cos]])

            d1 = np.array([[x],[y]])

            A = np.dot(R,a)+d1
            B = np.dot(R,b)+d1
            C = np.dot(R,c)+d1
            D = np.dot(R,d)+d1

            x1 = A[0,0]
            y1 = A[1,0]
            x2 = B[0,0]
            y2 = B[1,0]
            x3 = C[0,0]
            y3 = C[1,0]
            x4 = D[0,0]
            y4 = D[1,0]

            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x2,y2, x2+Trp_size,y2+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x3,y3, x3+Trp_size,y3+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x4,y4, x4+Trp_size,y4+Trp_size), fill = (0,0,0), width = 0)
            im.save(Dir+'/Image'+str(j)+'.png')

            i +=res
            j+=1
        exec(open("upload_V2.py").read())
        x = x1-r
        y = y1
        move()

    if user == 'down':
        i=0
        j=0
        while i < res*10:
            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)
            if i == 0:
                sin = np.sin(int(theta)*3.1416/180)
                cos = np.cos(int(theta)*3.1416/180)
            elif i == res:
                sin = np.sin(-int(theta)*3.1416/180)
                cos = np.cos(-int(theta)*3.1416/180)

            x1=r
            y1=i
            x2=-r
            y2=0+i
            x3=0
            y3=r+i
            x4=0
            y4=-r+i

            sin = np.sin(int(theta)*3.1416/180)
            cos = np.cos(int(theta)*3.1416/180)

            a = np.array([[x1],[y1]])
            b = np.array([[x2],[y2]])
            c = np.array([[x3],[y3]])
            d = np.array([[x4],[y4]])

            R = np.array([[cos, -sin],
                [sin, cos]])

            d1 = np.array([[x],[y]])

            A = np.dot(R,a)+d1
            B = np.dot(R,b)+d1
            C = np.dot(R,c)+d1
            D = np.dot(R,d)+d1

            x1 = A[0,0]
            y1 = A[1,0]
            x2 = B[0,0]
            y2 = B[1,0]
            x3 = C[0,0]
            y3 = C[1,0]
            x4 = D[0,0]
            y4 = D[1,0]
            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x2,y2, x2+Trp_size,y2+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x3,y3, x3+Trp_size,y3+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x4,y4, x4+Trp_size,y4+Trp_size), fill = (0,0,0), width = 0)



            im.save(Dir+'/Image'+str(j)+'.png')

            i +=res
            j +=1
        exec(open("upload_V2.py").read())
        x = x1-r
        y = y1
        move()

    if user == 'up':
        i=0
        j=0
        while i < res*10:
            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)
            if i == 0:
                sin = np.sin(int(theta)*3.1416/180)
                cos = np.cos(int(theta)*3.1416/180)
            elif i == res:
                sin = np.sin(-int(theta)*3.1416/180)
                cos = np.cos(-int(theta)*3.1416/180)

            x1=r
            y1=0-i
            x2=-r
            y2=0-i
            x3=0
            y3=r-i
            x4=0
            y4=-r-i

            sin = np.sin(int(theta)*3.1416/180)
            cos = np.cos(int(theta)*3.1416/180)

            a = np.array([[x1],[y1]])
            b = np.array([[x2],[y2]])
            c = np.array([[x3],[y3]])
            d = np.array([[x4],[y4]])

            R = np.array([[cos, -sin],
                [sin, cos]])

            d1 = np.array([[x],[y]])

            A = np.dot(R,a)+d1
            B = np.dot(R,b)+d1
            C = np.dot(R,c)+d1
            D = np.dot(R,d)+d1

            x1 = A[0,0]
            y1 = A[1,0]
            x2 = B[0,0]
            y2 = B[1,0]
            x3 = C[0,0]
            y3 = C[1,0]
            x4 = D[0,0]
            y4 = D[1,0]

            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x2,y2, x2+Trp_size,y2+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x3,y3, x3+Trp_size,y3+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x4,y4, x4+Trp_size,y4+Trp_size), fill = (0,0,0), width = 0)
            im.save(Dir+'/Image'+str(j)+'.png')

            #exec(open("upload_V2.py").read())
            i +=res
            j+=1
        exec(open("upload_V2.py").read())
        x = x1-r
        y = y1
        move()

    if user == 'CW':

        theta = input('Insert an angle')
        if rt == 0:
            th = theta
            i=0
            j=0
        else:
            th = int(theta) + int(rt)
            i = rt
            j=0

        while i <= int(th):

            sin = np.sin(int(i)*3.1416/180)
            cos = np.cos(int(i)*3.1416/180)

            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)

            x1=r
            y1=0
            a = np.array([[x1],[y1]])

            x2=-r
            y2=0
            b = np.array([[x2],[y2]])

            x3=0
            y3=r
            c = np.array([[x3],[y3]])

            x4=0
            y4=-r
            d = np.array([[x4],[y4]])


            R = np.array([[cos, -sin],
                [sin, cos]])

            d1 = np.array([[x],[y]])

            A = np.dot(R,a)+d1
            B = np.dot(R,b)+d1
            C = np.dot(R,c)+d1
            D = np.dot(R,d)+d1

            x1 = A[0,0]
            y1 = A[1,0]
            x2 = B[0,0]
            y2 = B[1,0]
            x3 = C[0,0]
            y3 = C[1,0]
            x4 = D[0,0]
            y4 = D[1,0]


            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x2,y2, x2+Trp_size,y2+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x3,y3, x3+Trp_size,y3+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x4,y4, x4+Trp_size,y4+Trp_size), fill = (0,0,0), width = 0)
            im.save(Dir+'/Image'+str(j)+'.png')

            i += (res-13)
            j +=1

        #Upload V2

        d = 1 #initial delay in seconds
        N = j  # the value 9 depends on the last name of the test pattern form drawing_v5



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
            time.sleep(1)

            i+=1  #exec(open("upload_V2.py").read())

        x = (x3+x4)/2
        y = (y3+y4)/2

        rt = i
        move()

    if user == 'CCW':

        theta = input('Insert an angle')
        if rt == 0:
            th = theta
            i=0
            j=0
        else:
            th = int(theta) + int(rt)
            i = rt
            j=0

        while i <= int(th):

            sin = np.sin(-int(i)*3.1416/180)
            cos = np.cos(-int(i)*3.1416/180)

            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)

            x1=r
            y1=0
            a = np.array([[x1],[y1]])

            x2=-r
            y2=0
            b = np.array([[x2],[y2]])

            x3=0
            y3=r
            c = np.array([[x3],[y3]])

            x4=0
            y4=-r
            d = np.array([[x4],[y4]])


            R = np.array([[cos, -sin],
                [sin, cos]])

            d1 = np.array([[x],[y]])

            A = np.dot(R,a)+d1
            B = np.dot(R,b)+d1
            C = np.dot(R,c)+d1
            D = np.dot(R,d)+d1

            x1 = A[0,0]
            y1 = A[1,0]
            x2 = B[0,0]
            y2 = B[1,0]
            x3 = C[0,0]
            y3 = C[1,0]
            x4 = D[0,0]
            y4 = D[1,0]


            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x2,y2, x2+Trp_size,y2+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x3,y3, x3+Trp_size,y3+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x4,y4, x4+Trp_size,y4+Trp_size), fill = (0,0,0), width = 0)
            im.save(Dir+'/Image'+str(j)+'.png')

            i += (res-13)
            j +=1

        #Upload V2

        d = 1 #initial delay in seconds
        N = j  # the value 9 depends on the last name of the test pattern form drawing_v5



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
            time.sleep(1)

            i+=1   # this value depends on the increment of the test pattern obtained from drawing_v5

        x = (x3+x4)/2
        y = (y3+y4)/2

        rt = i
        move()



move()

# user =  input('Which way?')
# exec(open("drawing_v4.py").read())
#im.save(Dir+'/Image'+str(1)+'.png')
