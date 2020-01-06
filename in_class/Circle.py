import graphics as gs
import time
#from graphics import *

window = gs.GraphWin("name me!", 600,400)

myCircle = gs.Circle(gs.Point(10,20),5)
myCircle.draw(window)


myCircle2 = myCircle.clone()
myCircle2.setFill("red")
myCircle2.draw(window)
for i in range(100):
	time.sleep(.1)
	myCircle2.move(1,0)


input("Enter to quit")
#myCircle = Circle(Point(10,20),5)