from PIL import Image, ImageDraw, ImageFont
import math
from pynput.keyboard import Key, Controller
keyboard = Controller()
canvas = (1920, 1200) #resolution of the SLM

Dir = r'C:\Users\mjamil\OneDrive - University of Massachusetts Dartmouth\Python Control\Test Patterns'
# im = Image.new('RGBA', canvas, (255, 255, 255, 255))
# draw = ImageDraw.Draw(im)
#declaring the initial position of the tra[p]
# global x
# global y
x = 1200
y = 600

i=0 #this is not required

Trp_size = 30
res = 20 # resolution of the movement of the


def move():

    user =  input('Which way?')



    if user == 'right':
        i=0
        while i < res*10:
            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)
            global x
            global y
            x1=x+i
            y1=y
            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            im.save(Dir+'/Image'+str(i)+'.png')

            i +=res

        exec(open("upload_V2.py").read())    
        x = x1 #saving the previous coordinates
        y = y1
        move()

    if user == 'left':
        i=0
        while i < res*10:
            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)

            x1=x-i
            y1=y
            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            im.save(Dir+'/Image'+str(i)+'.png')
            i +=res
        exec(open("upload_V2.py").read())
        x = x1
        y = y1
        move()

    if user == 'down':
        i=0
        while i < res*10:
            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)
            x1=x
            y1=y+i
            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            im.save(Dir+'/Image'+str(i)+'.png')

            #exec(open("object_tracking.py").read())
            i +=res
        exec(open("upload_V2.py").read())
        x = x1
        y = y1
        move()

    if user == 'up':
        i=0
        while i < res*10:
            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)
            x1=x
            y1=y-i
            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            im.save(Dir+'/Image'+str(i)+'.png')

            #exec(open("object_tracking.py").read())
            i +=res
        exec(open("upload_V2.py").read())
        x = x1
        y = y1
        move()

move()

# user =  input('Which way?')
# exec(open("drawing_v4.py").read())
#im.save(Dir+'/Image'+str(1)+'.png')
