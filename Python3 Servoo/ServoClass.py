import RPi.GPIO as GPIO
import time

freqHz = 50
msPerCycle = 1000/freqHz

def setupServos(pin1, pin2, width, height):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    servo1 = Servo(GPIO.PWM(pin1, freqHz))
    servo2 = Servo(GPIO.PWM(pin2, freqHz))
    return Servos(servo1, servo2, width, height)

def mapTo(var, input_low, input_high, output_low, output_high):
    var = minmax(var, input_low, input_high)
    slope = float(float(output_high - output_low) / float(input_high - input_low))
    output = output_low + slope * (var - input_low)
    return output

def minmax(var, low, high):
    var = min(var, high)
    var = max(var, low)
    return var

max_right = .89
max_left = 1.83
middle = 1.36

class Servo:
    
    Min = 1.19
    Max = 1.53
    
    MinPerc = 0
    MaxPerc = 1
    
    def __init__(self, pwm, Min, Max):
        self.pwm = pwm
        self.Min = Min
        self.Max = Max

    def __init__(self, pwm):
        self.pwm = pwm

    def minmax(self, Min, Max):
        self.Min = minmax(Min, max_right, max_left)
        self.Max = minmax(Max, max_right, max_left)

    def goto(self, perc, sleep):
        print(perc)
        perc = minmax(perc, 0, 1)
        perc = 1 - perc
        pos = mapTo(perc, 0, 1, self.Min, self.Max)
        pos = mapTo(perc, 0, 1, self.Min, self.Max)
        self.moveTo(pos, sleep)

    def moveTo(self, pos, sleep):
        print(pos)
        dutyCyclePerc = pos * 100 / msPerCycle
        self.pwm.start(dutyCyclePerc)
        time.sleep(sleep)

class Servos:
    width = 1000
    height = 1000
    
    def __init__(self, servo1, servo2, width, height):
        self.x = servo1
        self.y = servo2
        # need to set restrictions on x/y range based on w/h
        self.Width = width
        self.Height = height
        #self.goto(.5, .5, 1)
        print("Setup complete. Width =", width, "Height =", height)

    def minmax(self, Min, Max):
        self.x.Min = minmax(Min, max_right, max_left)
        self.x.Max = minmax(Max, max_right, max_left)
        
        self.y.Min = minmax(Min, max_right, max_left)
        self.y.Max = minmax(Max, max_right, max_left)

    def goto(self, x, y, wait):
        x = mapTo(x, self.x.MinPerc, self.x.MaxPerc, self.x.Min, self.x.Max)
        y = mapTo(y, self.y.MinPerc, self.y.MaxPerc, self.y.Min, self.y.Max)
        self.x.moveTo(x, 0)
        self.y.moveTo(y, wait)

    def moveTo(self, x, y, wait):
        print("Moving to ("+str(x)+", "+str(y)+")")
        x = int(self.width - x)
        y = int(self.height - y)
        x = mapTo(x, 0, self.Width, self.x.MinPerc, self.x.MaxPerc)
        y = mapTo(y, 0, self.Height, self.y.MinPerc, self.y.MaxPerc)
        print(x,y)
        self.goto(x, y, wait)

    def wait(self, wait):
        time.sleep(wait)

    def cleanup(self):
        self.x.goto(.5, .5)
        self.y.goto(.5, .5)
        time.sleep(.5)
        GPIO.cleanup()
