#Calculating the area of a rectangle

#AreaOfRectangle.py

#Author: Robert S. Soto
#Date: July 23, 2020

from tkinter import *
from tkinter import ttk

class AreaRectangle:
    def __init__(self):
        self.window = Tk()
        self.window.title("Area of a Rectangle")
        self.build_widgets()

    def build_widgets(self):
        self.window['padx'] = 8
        self.window['pady'] = 8

        forTitle = ttk.Label(self.window, text='Area of a Rectangle')
        forTitle.grid(row=0, column=1)

        blank_space = ttk.Label(self.window, text='')
        blank_space.grid(row=1)

        forWidth = ttk.Label(self.window, text='Width')
        forWidth.grid(row=2)
        self.w = Entry(self.window)
        self.w.grid(row=2, column=1)

        forLength = ttk.Label(self.window, text='Length')
        forLength.grid(row=3)
        self.l = Entry(self.window)
        self.l.grid(row=3, column=1)

        calculate = ttk.Button(self.window, text='Calculate', command=self.Calculate_Area)
        calculate.grid(row=4, column=1)

        self.Area_out = ttk.Label(self.window, text='Area: ')
        self.Area_out.grid(row=3, column=3)

        quit_out = ttk.Button(self.window, text='Quit', command=self.window.destroy)
        quit_out.grid(row=4,column=2)
        
    def Calculate_Area(self):
        W = int(self.w.get())
        L = int(self.l.get())
        output = '%d'%(W*L)
        self.Area_out['text'] = output

interact = AreaRectangle()
interact.window.mainloop()
