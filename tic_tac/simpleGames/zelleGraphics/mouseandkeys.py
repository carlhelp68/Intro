# written by David Liben-Nowell
# modified by Sherri Goings
# last modified 5/2017
# project.py
#
# A sample chunk of code to support the handling of mouse clicks and
# key presses in real time (ish) using Zelle graphics.
# 
# Initial behavior: creates window with "reset" box in upper right corner and
# one blue filled circle that moves slowly to the right in the window
#
# Things you can do:
# 0. click on the usual x in the upper right of the window to exit the simulation
# 1. click anywhere in the "reset" square - resets the screen back to the initial
# state (almost) and simulation starts over
# 2. click anywhere else - creates small circle that moves down quickly, circle will
# be red if click to left of current position of main blue circle, or green if click
# to right of main blue circle
# 3. press the space-bar - same reset behavior as clicking in reset square
# 4. press the "q" key - some text appears stating to click the upper right x to quit game
# 5. press the down arrow key - moves all circles on screen down a bit
# 6. press any other key - displays key pressed in upper left of window
#

from graphics import *
import random
import time

class clickableWindow:
    def __init__(self):
        self.window = GraphWin("Game Sample",800,600)
        self.window.setMouseHandler(self.handleClick)
        self.window.master.bind("<Key>",self.handleKeyPress)
        self.lastkey = None
        self.lastupdate = time.time()
        self.startScreen()

    # split into own function to keep organized and to allow user to return
    # to start screen at any time without creating whole new window
    def startScreen(self):
        reset = Rectangle(Point(700,10),Point(750,60))
        reset.draw(self.window)
        txt = Text(Point(725,35), "RESET")
        txt.setTextColor("blue")
        txt.draw(self.window)
        self.circle = Circle(Point(100,100),10)
        self.circle.setFill(color_rgb(0,0,0))
        self.circle.draw(self.window)
        self.circle.setFill('blue')
        self.clicks = []

    def reset(self):
        self.circle.undraw()
        for clic in self.clicks:
            clic.undraw()
        if self.lastkey:
            self.lastkey.undraw()
        self.startScreen()
        
    # Do some processing "every once in a while" -- if it's been a
    # least .025 seconds since the circle in
    # this window was redrawn, redraw it with a slight move of all circles.
    # This is better than doing some stuff and then using sleep to pause for some
    # amount of time, because the program while sleeping can't handle input like key
    # presses and mouse clicks
    def update(self):
        if time.time() - self.lastupdate > 0.025:
        	# move main circle slowly to the right
            self.circle.move(1,0)
            # move all mouseclick created circles quickly down
            for clic in self.clicks:
                clic.move(0,5)
            self.lastupdate = time.time()
        self.window.update()

    # Returns True if and only if this window has been closed.
    def closed(self):
        return not self.window.winfo_exists()        

    def handleClick(self,point):
        """ This code will be executed whenever the left mouse button is
        clicked, and the value passed in as point will be the
        location on the screen where the click occurred. You can get the
        x and y coordinates via point.getX() and point.getY(). """
        # First check if click inside "reset" box, if so reset and end this function now
        if 700 < point.getX() < 750 and 10 < point.getY() < 60:
            self.reset()
            return
        
        # For fun, I've chosen to display a red circle at the point of the
        # click if it's to the left of the main blue circle, or green if it's
        # to the right. 
        c = Circle(point,5)
        if point.getX() < self.circle.getCenter().getX():
            c.setFill(color_rgb(255,0,0))
        else:
            c.setFill(color_rgb(0,255,0))            
        c.draw(self.window)
        self.clicks.append(c)

    def handleKeyPress(self,key):
        # This code will be executed whenever a key is pressed, and
        # the value passed in as key will represent the key that was
        # pressed.  You can get the character representing the pressed
        # key using key.char.  For kicks, I've chosen to display the
        # last pressed key in a text box at the upper left of the
        # window, by undrawing the previous text and then writing the
        # new text.  If the character is 'q', then the program quits.
        # If the character is the down arrow key, all objects move down on the screen
        if key.char == "q":
            Text(Point(100,50),"close the window to quit").draw(self.window)
        # note I got the correct string name for the down arrow by simply printing the 
        # "keysym" of whatever key I pressed on the keyboard and seeing what came out.
        elif key.keysym == "Down":
            self.circle.move(0,10)
            for clic in self.clicks:
                clic.move(0,10)
        elif key.keysym == "space":
            self.reset()
        else:
            print (key.char, key.keysym)
            if self.lastkey:
                self.lastkey.undraw()
            t = Text(Point(20,20),key.keysym)
            t.draw(self.window)
            self.lastkey = t


def main():
    print("Close the window to quit.")
    win = clickableWindow()
    
    
    # just call update() repeatedly until user quits by closing the window
    # don't include sleep as have in the past because rate of animation is standardized
    # in a better way in the update() function itself
    while not win.closed():
        win.update()

if __name__=="__main__":
    main()


