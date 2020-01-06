#
# Example code using pygame for a simple action-type "game"
# Author: Sherri Goings
# Last Modified: 05/2016
#

import pygame
from random import *

def getRandColor():
    """ returns an rgb tuple with random values between 0 and 255 """
    return (randrange(0,256), randrange(0,256), randrange(0,256))

class targetPractice:
    """ overall game class """
    
    def __init__(self, numBoxes, winWidth, winHeight):
        """ game constructor. Takes arguments:
              number of target boxes,
              width of game window,
              height of game window
        initializes crossHairs and given number of target boxes with 
        random parameters """
        
        self.cross = crossHairs(50, (100,0,50), (winWidth/2, winHeight/2), 
        	(0, winWidth), (0, winHeight))
        self.crossMoving = False

        self.numBoxes = numBoxes
        self.boxes = []
        # initialize boxes with different colors, sizes, speeds, and start pos
        # all boxes have same bounds (width and height of window)
        for i in range(numBoxes):
            size = randrange(20,50)
            color = getRandColor()
            pos = (randrange(0,winWidth-size), randrange(0,winHeight-size))
            speed = (randrange(1,4))
            newBox = movingBox(size, color, pos, speed, 
                               (0, winWidth), (0, winHeight))
            self.boxes.append(newBox)

        # start with 3 lives
        self.lives = 3

    def gameOver(self):
        """ game ends if have no more lives """
        return self.lives == 0

    def endScreen(self, screen):
        """ print gameover message and final score to game window """
        myfont = pygame.font.SysFont("Cambria", 46)
        endLine1 = myfont.render("GAME OVER", 1, (75, 0, 75))
        myfont = pygame.font.SysFont("Cambria", 28)
        endLine2 = myfont.render("Final Score: 000", 1, (75, 0, 75))
        screen.blit(endLine1, (200, 100))
        screen.blit(endLine2, (200, 200))
        pygame.display.flip()
        
    
    def handleEvent(self, event):
        """ checks for left mouse button press/release, mouse motion, 
        and spacebar press and takes appropriate action for each """
        
        # if user presses space when crosshairs are inside a box, 
        # change its color to a random new color,
        # If crosshairs were outside a box, take away a life.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            crossPos = self.cross.getPos()
            miss = True
            # check each box to see if crosshairs were within its bounds
            for box in self.boxes:
                boxPos = box.getPos()
                boxSide = box.getSideLength()
                if (boxPos[0] < crossPos[0] < boxPos[0]+boxSide) \
                	and (boxPos[1] < crossPos[1] < boxPos[1]+boxSide):
                    box.changeColor()
                    miss = False
            if miss:
                self.lives -= 1

        # if user presses the left mouse button, set moving to True, 
        # so the crosshairs will now follow the mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.crossMoving = True

        # if user releases the left mouse button, set moving to False, 
        # so the crosshairs will stop following the mouse
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.crossMoving = False

        # if the mouse moves, and moving is true (which means the left mouse
        # button is being held down), move the crosshairs to the mouse coords
        if event.type == pygame.MOUSEMOTION and self.crossMoving:
            self.cross.updatePos(event.pos)

        # if user presses P, pause the game until pressed again
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            event = pygame.event.poll()
            while not (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
                event = pygame.event.poll()
            

    def draw(self, screen):
        """ draws the crosshairs, all boxes, and num lives """
        self.cross.draw(screen)
        for box in self.boxes:
            box.draw(screen)
        myfont = pygame.font.SysFont("Cambria", 22)
        lives = myfont.render("LIVES: "+str(self.lives), 1, (75, 0, 75))
        screen.blit(lives, (20,20))
            
    def moveTargets(self):
        """ moves all of the target boxes 1 step """
        for box in self.boxes:
            box.moveStep()

    
class movingBox:
    """ class that represents a simple square that can move around the screen """
    def __init__(self, sideLength, color, initPos, speed, boundsX, boundsY):
        """ movingBox constructor. Takes arguments:
              length of side of the square box
              color to fill the box
              tuple or list with x,y coordinates of initial position
              speed at which box will move (how many pixels per step)
              tuple or list with min,max allowed x coordinates for the box to occupy
              tuple or list with min,max allowed y coordinates for the box to occupy """
        
        self.sideLength = sideLength
        self.pos = list(initPos)
        self.color = color
        self.speed = speed
        self.dir = [1,1]
        self.boundsX = boundsX
        self.boundsY = boundsY

    def draw(self, screen):
        """ draws the box to the screen """
        pygame.draw.rect(screen, self.color, 
        	(self.pos[0], self.pos[1], self.sideLength, self.sideLength))

    def moveStep(self):
        """ moves the box one step in its current direction, unless it hits a wall in 
        	which case it changes the current direction """
        if self.pos[0] <= self.boundsX[0] or \
        	(self.pos[0]+self.sideLength) >= self.boundsX[1]:
            	self.dir[0] *= -1
        if self.pos[1] <= self.boundsY[0] or \
        	(self.pos[1]+self.sideLength) >= self.boundsY[1]:
            	self.dir[1] *= -1
            
        self.pos[0] += self.dir[0]*self.speed
        self.pos[1] += self.dir[1]*self.speed

    def getSideLength(self):
        return self.sideLength

    def getPos(self):
        return self.pos

    def changeColor(self):
        self.color = getRandColor()
       

class crossHairs:
    """ class to represent the crosshairs of a gun """
    def __init__(self, length, color, initPos, boundsX, boundsY):
        """ crossHairs constructor. Takes arguments:
              radius of crosshairs 
              color to draw crosshairs
              tuple or list with x,y coordinates of initial position
              tuple or list with min,max allowed x coordinates for the box to occupy
              tuple or list with min,max allowed y coordinates for the box to occupy """

        self.length = length
        self.color = color
        self.pos = list(initPos)
        self.moving = False
        self.boundsX = boundsX
        self.boundsY = boundsY
        
    def draw(self, screen):
        """ draw crosshairs with 2 lines """
        pygame.draw.line(screen, self.color, 
        	(self.pos[0]-50,self.pos[1]),(self.pos[0]+50,self.pos[1]))
        pygame.draw.line(screen, self.color, 
        	(self.pos[0],self.pos[1]-50),(self.pos[0],self.pos[1]+50))
        
    def updatePos(self, mouse):
        """ move crosshairs position to the position of the given mouse coordinates """
        if mouse[0] > (self.boundsX[0]+self.length) and \
        	mouse[0] < (self.boundsX[1]-self.length):
            	self.pos[0] = mouse[0]
        if mouse[1] > (self.boundsY[0]+self.length) and \
        	mouse[1] < (self.boundsY[1]-self.length):
            	self.pos[1] = mouse[1]

    def getPos(self):
        return self.pos

                
def main():
    """ plays targetPractice game """

    # sets up all pygame modules for use
    pygame.init()
    
    # set up window with given width, height, and caption
    winWidth, winHeight = 640, 600
    screen = pygame.display.set_mode((winWidth, winHeight))
    pygame.display.set_caption("Exploring mouse, keys, and event loops with Pygame")

    # initialize parameters and draw just background screen
    running = 1
    bgcolor = (100,100,250)
    screen.fill(bgcolor)

    # create a new targetPractice game with 5 targets and draw initial game screen
    game = targetPractice(5, winWidth, winHeight)
    game.draw(screen)
    
    # add text box
    insts = ["Instructions: Hold down the left mouse button while sliding", 
    	"the mouse to move the crosshairs. Press the space bar with",
    	"the cross hairs inside of a square to change the color."]
    myfont = pygame.font.SysFont("Cambria", 22)
    instsLine1 = myfont.render(insts[0], 1, (75, 0, 75))
    instsLine2 = myfont.render(insts[1], 1, (75, 0, 75))
    instsLine3 = myfont.render(insts[2], 1, (75, 0, 75))
    instsLine4 = myfont.render("Hit P at any time to pause.", 1, (75, 0, 75))
    myfont = pygame.font.SysFont("Cambria", 28)
    instsLine5 = myfont.render("PRESS RETURN TO BEGIN", 1, (75, 0, 75))
    screen.blit(instsLine1, (50, 100))
    screen.blit(instsLine2, (50, 125))
    screen.blit(instsLine3, (50, 150))
    screen.blit(instsLine4, (175, 180))
    screen.blit(instsLine5, (150, 210))
    pygame.display.flip()

    # create the graphics clock
    clock = pygame.time.Clock()

    # continuously poll to see if the user has pressed the return key 
    # (an event has occurred of the type KEYDOWN meaning some key was pressed), so then 
    # check the specific event.key to see if it was the RETURN key.
    event = pygame.event.poll()
    while not (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
        # checks for the close button in the window being pressed
        if event.type == pygame.QUIT:
            quit()
        clock.tick(50)
        event = pygame.event.poll()
        

    # Now continue until user clicks x to close window
    while event.type != pygame.QUIT:
        
        # start by "erasing" everything by painting screen with background color
        screen.fill(bgcolor)

        # deal with any user input (keypress or mouseclick) that has occurred 
        # since last frame 
        game.handleEvent(event)

        # if last life was just lost, quit game loop
        if game.gameOver():
            game.endScreen(screen)
            break

        # move the target boxes one step each
        game.moveTargets()

        # draw the boxes and crosshairs at the appropriate current positions
        game.draw(screen)

        # show the new screen drawn
        pygame.display.flip()

        # sets frames/second so that game speed so will be same on all computers
        # values 20 - 80 are reasonable, a bigger number means faster game
        clock.tick(50)

        # get next event
        event = pygame.event.poll()

    # Keep showing game over screen until user clicks x to close window
    while event.type != pygame.QUIT:
        event = pygame.event.poll()


if __name__=="__main__":
    main()

