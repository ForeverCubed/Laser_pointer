#import tkinter as tk
from tkinter import *

class Window:
    master = Tk()

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.master.geometry(str(width)+"x"+str(height))
    
    def addButton(self, name, x, y, w, h, callback):
        b = Button(self.master, text=name, width=w, height=h, command=callback)
        b.pack()
    #def addButton(self, x, y, w, h, callback):
        #self.addButton("",x,y,w,h,callback)
    #def addButton(self, w, h, callback):
        #self.addButton("",0,0,w,h,callback)
    #def addButton(self, x, y, callback):
        #self.addButton("",x,y,60,20,callback)
    #def addButton(self, callback):
        #self.addButton("",0,0,60,20,callback)
        
    def mainloop(self):
        self.master.mainloop()
