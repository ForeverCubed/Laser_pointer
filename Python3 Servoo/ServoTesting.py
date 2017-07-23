import ServoClass
import Servo_testers as test
#import tk_setup as tk
import tkinter as tk
import math
width, height = 500,500

#servos = ServoClass.setupServos(11, 12, width, height)

#servos.minmax(1.17, 1.51)

window = tk.Tk()
window.geometry("600x400")
try: # here is the main body of the code
    print("Entering main block")
    def bPress():
        print("Click!")

    b = tk.Button(window, command=bPress)
    
    window.master.mainloop()
except TypeError:
    print("TypeError in main")
except AttributeError:
    print("AttributeError in main")

#servos.cleanup()
print("Done!")


#servos.x.minmax(1.21, 1.51)
#servos.y.minmax(1.3, 1.49)
#size = 200
#test.square(servos, (width/2-size/2), (height/2-size/2), size)
