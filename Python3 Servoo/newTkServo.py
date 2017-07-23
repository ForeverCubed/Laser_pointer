import tkinter as tk
from tkinter import *
import time
import ServoClass
width, height = 800,400

servos = ServoClass.setupServos(11, 12, width, height)

servos.x.minmax(1.23, 1.51)
servos.y.minmax(1.21, 1.49)

try:
    top = tk.Tk()
    top.geometry(str(width)+"x"+str(height))
    
    def callback(event):
        servos.moveTo(event.x, event.y, .1)
        
    frame = tk.Frame(top, width=width, height=height)
    
    frame.bind("<Button-1>", callback)
    frame.bind("<B1-Motion>", callback)

    frame.pack()
    top.mainloop()
              
except TypeError:
    print("TypeError in main")

servos.cleanup()
print("Done!")
