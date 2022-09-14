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
x = 960
y = 600

i=0 #this is not required

Trp_size = 30
res = 10 # resolution of the movement of the traps


def move():

    user =  input('Which way?')



    if user == 'right':
        i=0
        while i < res*10:
            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)
            global x
            global y
            x1=x+240+i
            y1=y
            x2=x-240+i
            y2=y
            x3=x+i
            y3=y+240
            x4=x+i
            y4=y-240
            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x2,y2, x2+Trp_size,y2+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x3,y3, x3+Trp_size,y3+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x4,y4, x4+Trp_size,y4+Trp_size), fill = (0,0,0), width = 0)
            im.save(Dir+'/Image'+str(i)+'.png')

            i +=res

        #exec(open("upload_V2.py").read())
        x = x1-240 #saving the previous coordinates
        y = y1
        move()

    if user == 'left':
        i=0
        while i < res*10:
            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)

            x1=x+240-i
            y1=y
            x2=x-240-i
            y2=y
            x3=x-i
            y3=y+240
            x4=x-i
            y4=y-240
            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x2,y2, x2+Trp_size,y2+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x3,y3, x3+Trp_size,y3+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x4,y4, x4+Trp_size,y4+Trp_size), fill = (0,0,0), width = 0)
            im.save(Dir+'/Image'+str(i)+'.png')

            i +=res

        #exec(open("upload_V2.py").read())
        x = x1-240
        y = y1
        move()

    if user == 'down':
        i=0
        while i < res*10:
            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)

            x1=x+240
            y1=y+i
            x2=x-240
            y2=y+i
            x3=x
            y3=y+240+i
            x4=x
            y4=y-240+i
            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x2,y2, x2+Trp_size,y2+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x3,y3, x3+Trp_size,y3+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x4,y4, x4+Trp_size,y4+Trp_size), fill = (0,0,0), width = 0)



            im.save(Dir+'/Image'+str(i)+'.png')

            #exec(open("object_tracking.py").read())
            i +=res
        #exec(open("upload_V2.py").read())
        x = x1-240
        y = y1
        move()

    if user == 'up':
        i=0
        while i < res*10:
            im = Image.new('RGBA', canvas, (255, 255, 255, 255))
            draw = ImageDraw.Draw(im)
            x1=x+240
            y1=y-i
            x2=x-240
            y2=y-i
            x3=x
            y3=y+240-i
            x4=x
            y4=y-240-i
            draw.ellipse((x1,y1, x1+Trp_size,y1+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x2,y2, x2+Trp_size,y2+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x3,y3, x3+Trp_size,y3+Trp_size), fill = (0,0,0), width = 0)
            draw.ellipse((x4,y4, x4+Trp_size,y4+Trp_size), fill = (0,0,0), width = 0)
            im.save(Dir+'/Image'+str(i)+'.png')

            #exec(open("object_tracking.py").read())
            i +=res
        exec(open("upload_V2.py").read())
        x = x1-240
        y = y1
        move()

move()

# user =  input('Which way?')
# exec(open("drawing_v4.py").read())
#im.save(Dir+'/Image'+str(1)+'.png')
