import RPi.GPIO as GPIO
import time
import ServoClass
import tkinter as tk
from tkinter import *

width, height = 600,600

def mapTo(var, input_low, input_high, output_low, output_high):
    slope = float(float(output_high - output_low) / float(input_high - input_low))
    output = output_low + slope * (var - input_low)
    return output

freqHz = 50
pin1 = 11
pin2 = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

servo1 = ServoClass.Servo(GPIO.PWM(pin1, freqHz))
servo2 = ServoClass.Servo(GPIO.PWM(pin2, freqHz))



top = tk.Tk()
top.geometry(str(width)+"x"+str(height))

def callback(event):
    print("click at",event.x,event.y)
    x = mapTo(event.x, 0, width, 0, 1)
    y = mapTo(event.y, 0, height, 0, 1)
    print("moving servos to",x,y)
    servo1.moveTo(x,0)
    servo2.moveTo(y,1)
    

frame = tk.Frame(top, width=width, height=height)
frame.bind("<Button-1>", callback)

frame.pack()
top.mainloop()

servo1.moveTo(.5, 0)
servo2.moveTo(.5, .5)
GPIO.cleanup()
print("Done!")
