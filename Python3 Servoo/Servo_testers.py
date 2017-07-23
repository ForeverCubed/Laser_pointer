import math

def corners(servos, count):
    width = servos.Width
    height = servos.Height
    
    servos.moveTo(0, 0, 1)
    servos.moveTo(0, height, 1)
    servos.moveTo(width, height, 1)
    servos.moveTo(width, 0, 1)
    servos.moveTo(0, 0, 1)

def circle(servos):
    width = servos.Width
    height = servos.Height
    
    r = 300
    theta = 1
    count = 0
    while count < 30:
        x = width/2 + r * math.cos(math.radians(theta))
        y = height/2 + r * math.sin(math.radians(theta))
        servos.moveTo(int(x), int(y), .2)
        theta += 35
        count += 1
def square(servos, x, y, size):
    width = servos.Width
    height = servos.Height

    servos.moveTo(x, y, 1)
    servos.moveTo(x+size, y, 1)
    servos.moveTo(x+size, y+size, 1)
    servos.moveTo(x, y+size, 1)
    servos.moveTo(x, y, 1)

def squares(servos, count):
    width = servos.Width
    height = servos.Height
    
    addw = width/count
    addh = height/count
    w = addw
    h = addh
    servos.moveTo(width/2, height/2, .5)

    for i in range(count):
        servos.moveTo(width/2-w/2, height/2-h/2, .4)
        servos.moveTo(width/2+w/2, height/2-h/2, .4)
        servos.moveTo(width/2+w/2, height/2+h/2, .4)
        servos.moveTo(width/2-w/2, height/2+h/2, .4)
        w += addw
        h += addh

def star(servos, count):
    width = servos.Width
    height = servos.Height
    
    points = [[-1, 2], [0, -2], [1, 2], [-2, 0], [2, 0]]
    mult = height/4
    wait = .5
    for i in range(count):
        for point in points:
            servos.moveTo(width/2+point[0]*mult, height/2+point[1]*mult, wait)




    
