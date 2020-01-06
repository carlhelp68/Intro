import graphics as gs
import time

window = gs.GraphWin("name me!", 600,400)

myrect = gs.Rectangle(gs.Point(20,20), gs.Point(40,60))
myrect.draw(window)
myrect1 = gs.Rectangle(gs.Point(20,20), gs.Point(120,10))
myrect1.draw(window)

myCircle = gs.Circle(gs.Point(110,15),5)
myCircle.draw(window)

for i in range(100):
	time.sleep(.01)
	myCircle.move(1,0)




input("Input Enter to continue")