#Convertions of distances and degrees

#converter.py

#Author: Robert S. Soto
#Date: July 22, 2020


from tkinter import *
from tkinter import ttk

class Converter():
    def __init__(self):
        self.window = Tk()
        self.window.title("Conversions")
        self.create_widgets()

    def create_widgets(self):
        self.window['padx'] = 7
        self.window['pady'] = 7

        forMiles = ttk.Label(self.window, text='Distance in Miles')
        forMiles.grid(row=1)
        self.e1 = ttk.Entry(self.window)
        self.e1.grid(row=1, column=1)  #for Miles
        
        forKilometers = ttk.Label(self.window, text='Distance in Kilometers')
        forKilometers.grid(row=2)
        self.e2 = ttk.Entry(self.window)
        self.e2.grid(row=2, column=1)  #for Kilometers

        forFarenheit = ttk.Label(self.window, text='Temperature in Farenheit')
        forFarenheit.grid(row=3)
        self.e3 = ttk.Entry(self.window)
        self.e3.grid(row=3, column=1)

        forCelsius = ttk.Label(self.window, text='Temperature in Celsius')
        forCelsius.grid(row=4)
        self.e4 = ttk.Entry(self.window)
        self.e4.grid(row=4, column=1)
        
        blank_space = Label(self.window, text=None)
        blank_space.grid(row=5)
        
        clear = ttk.Button(self.window, text='Clear', command=self.clearing_content)
        clear.grid(row=6, column=1)

        convert = ttk.Button(self.window, text='Convert', command=self.Distance_Convertion)
        convert.grid(row=7, column=1)

        quitting = ttk.Button(self.window, text='Quit', command=self.window.destroy)
        quitting.grid(row=7, column=0)

        self.miles_result = ttk.Label(self.window, text ='')
        self.miles_result.grid(row=1,column =2)

        self.kilometers_result = ttk.Label(self.window, text ='')
        self.kilometers_result.grid(row=2,column =2)

        self.faren_result = ttk.Label(self.window, text ='')
        self.faren_result.grid(row=3,column =2)

        self.celsius_result = ttk.Label(self.window, text ='')
        self.celsius_result.grid(row=4,column=2)

    def Distance_Convertion(self):
        m = float(self.e1.get())
        outputKilometers = "{0:0.2f} km".format(m*1.60934)
        self.miles_result['text'] = outputKilometers

        k = float(self.e2.get())
        outputMiles = "{0:0.2f} ml".format(k*0.621371)
        self.kilometers_result['text'] = outputMiles

        f = float(self.e3.get())
        outputCelsius = "{0:0.2f}°".format(((f-32) * 5/9))
        self.faren_result['text'] = outputCelsius

        c = float(self.e4.get())
        outputFarenheit = "{0:0.2f}°".format(((c*9/5) + 32))
        self.celsius_result['text'] = outputFarenheit
        
    def clearing_content(self):
        self.e1.delete(0, 'end')
        self.miles_result['text'] = ''

        self.e2.delete(0, 'end')
        self.kilometers_result['text'] = ''

        self.e3.delete(0, 'end')
        self.faren_result['text'] = ''

        self.e4.delete(0, 'end')
        self.celsius_result['text'] = ''


    #I could not resolve some impotant bugs in the program :(, for example when I tried just to convert one or two of them. But this is what I have, I could not spend
    #more time on it. It is 11:00 pm. I must study for the exam tomorrow.

drawing = Converter()
drawing.window.mainloop()
