#Drawing a house

#drawingHouse.py

#Author: Robert S. Soto
#Date: July 9, 2020

from tkinter import *
from time import sleep

def draw(canvas, width, height):
    canvas.create_rectangle(0,0, width,height/2, fill = 'sky blue')
    canvas.create_rectangle(0,height/2, width,height, fill = 'dark green')
    canvas.create_rectangle(width/2+50,height/2-50, width/2+300,height/2+100, fill = 'brown')
    canvas.create_rectangle(width/2+150,height/2+50, width/2+200,height/2+100, fill = "#%02x%02x%02x" % (226, 186,92))
    canvas.create_polygon((width/2,height/2-50), (width/2+50,height/2-100), (width/2+300,height/2-100), (width/2+350,height/2-50), fill= 'gray')
    sun = canvas.create_oval((25,25), (75,75), fill = 'yellow')

    timeDelay = 0.20
    for num in range(180):
        sleep(timeDelay)
        canvas.coords(sun,25+5*num, 25,75+5*num, 75)
        canvas.update()
    canvas.create_rectangle(0,0, width,height/2, fill = "#%02x%02x%02x" % (255, 196,55))
    canvas.create_rectangle(0,height/2, width,height, fill = 'dark green')
    canvas.create_rectangle(width/2+50,height/2-50, width/2+300,height/2+100, fill = 'brown')
    canvas.create_rectangle(width/2+150,height/2+50, width/2+200,height/2+100, fill = "#%02x%02x%02x" % (226, 186,92))
    canvas.create_polygon((width/2,height/2-50), (width/2+50,height/2-100), (width/2+300,height/2-100), (width/2+350,height/2-50), fill= 'gray')
    sun = canvas.create_oval((25,25), (75,75), fill = "#%02x%02x%02x" % (255, 255,102))
    canvas.coords(sun,25+5*num, 25,75+5*num, 75)
    canvas.update()
        
def runDrawing(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()#Tells the window to pack
                #the canvas within it.
    draw(canvas, width, height)
    root.mainloop()
    print("Bye!")

runDrawing(1000, 500)


#... In the end, I could not figure out the correct use of the coordinates on the window to draw the windows and maybe some clouds :(((
