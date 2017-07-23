import ServoClass
import Servo_testers as test
width, height = 1000,1000

servos = ServoClass.setupServos(11, 12, width, height)

servos.x.minmax(1.22, 1.50)
servos.y.minmax(1.21, 1.49)

try:
    print("Entering main block")
    #servos.moveTo(0, 0, 1)
    servos.y.moveTo(1.2, 1)
    #test.corners(servos, 1)
              
except TypeError:
    print("TypeError in main")

servos.cleanup()
print("Done!")
