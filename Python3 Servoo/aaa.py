import ServoClass
import Servo_testers as test
width, height = 1000,1000

servos = ServoClass.setupServos(11, 12, width, height)

servos.x.minmax(1.22, 1.50)
servos.y.minmax(1.21, 1.49)

try:
    print("Entering main block")
    servos.moveTo(width/2,height/2,2)
              
except TypeError:
    print("TypeError in main")

servos.cleanup()
print("Done!")
