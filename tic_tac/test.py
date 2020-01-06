"""authors: Eric Stadelman and Maya Collier"""
"""date: 5/21/17"""
"""Game plays tic tac toe"""

import graphics as gs
import random
import time


class clickableWindow:
    def __init__(self):
        """initializes all handle click and sets first player to X"""
        self.window = gs.GraphWin("Game Sample",900,900)
        self.window.setMouseHandler(self.handleClick)
        self.startScreen()
        self.currentplayer = "X" 
        
    
    def startScreen(self):
        """Draws game board and sets up grid for where we will put X or O for clicks"""
        self.horiz_line= gs.Line(gs.Point(0,300), gs.Point(900, 300))
        self.horiz_line2= gs.Line(gs.Point(0,600), gs.Point(900, 600))
        self.vert_line= gs.Line(gs.Point(300,0), gs.Point(300, 900))
        self.vert_line2= gs.Line(gs.Point(600,0), gs.Point(600, 900))
        self.horiz_line.draw(self.window)
        self.horiz_line2.draw(self.window)
        self.vert_line.draw(self.window)
        self.vert_line2.draw(self.window)
        self.grid = [[1,2,3],[4,5,6],[7,8,9]]
            
    def handleClick(self, point):
        """Handle click and sends cordinate to setText to be drawn, also checks if valid"""
        self.new_x=point.getX()
        self.new_y=point.getY()
        """Checks that cordinate doesnt already have X or O inside"""
        if self.grid[self.new_x//300][self.new_y//300] == "O" or self.grid[self.new_x//300][self.new_y//300] == "X" : 
            txt = gs.Text(gs.Point(725,35), "Invalid Click")
            txt.setTextColor("red")
            txt.draw(self.window)
            self.circle = gs.Circle(gs.Point(self.new_x,self.new_y),10)
            self.circle.setFill(gs.color_rgb(255,0,0))
            self.circle.draw(self.window)
            self.circle.setFill('red')
            return
        
        self.grid[self.new_x//300][self.new_y//300] = self.currentplayer
        self.setText()
    
        """Switches player from X to O or from O to X"""
        if self.currentplayer == "X":
            self.currentplayer="O"
        else:
            self.currentplayer="X"
        	
    def setText(self):
        """prints X or O to screen after click"""
        """takes x and y value and puts them into cordinate"""
        x=self.new_x//300
        y= self.new_y//300

        """Draws X or O to center of square"""
        if self.currentplayer == "X":
            txt=gs.Text(gs.Point(x * 300 + 150, y *300 + 150), "X")
            txt.setSize(35)
            txt.draw(self.window)

        else:
            txt=gs.Text(gs.Point(x *300 + 150, y *300 + 150), "O")
            txt.setSize(35)
            txt.draw(self.window)
        return txt
        
    def isWon(self):
        game_over=False
        X_counter = 0
        O_counter = 0
        game_over = 0
        reprint_x=0
        reprint_y=0
        for i in range(len(self.grid)):
            X_counter = 0
            O_counter = 0
            """Determines if the columns are X's"""
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == "X":
                    X_counter +=1
                    game_over +=1
                    if X_counter ==3:
                        for j in range(len(self.grid[i])):
                            reprint_x=i*300+150
                            reprint_y=j*300+150
                            txt=gs.Text(gs.Point(reprint_x, reprint_y), "X")
                            txt.setSize(35)
                            txt.setTextColor("red")
                            txt.draw(self.window)   
                        return "X"

                        """Determines if the columns are O's"""
                if self.grid[i][j] == "O":
                    O_counter +=1
                    game_over+=1
                    if O_counter == 3:
                        for j in range(len(self.grid[i])):
                            reprint_x=i*300+150
                            reprint_y=j*300+150
                            txt=gs.Text(gs.Point(reprint_x, reprint_y), "O")
                            txt.setSize(35)
                            txt.setTextColor("red")
                            txt.draw(self.window)
                        return "O"

        for i in range(len(self.grid)):
            X_counter = 0
            O_counter = 0
            """ Determines if the rows are X's"""
            for j in range(len(self.grid[i])):
                if self.grid[j][i] == "X":
                    X_counter +=1
                
                    if X_counter ==3:
                        for j in range(3):
                            reprint_x=j*300+150
                            reprint_y=i*300+150
                            txt=gs.Text(gs.Point(reprint_x, reprint_y), "X")
                            txt.setSize(35)
                            txt.setTextColor("red")
                            txt.draw(self.window)  
                        return "X"
                        """Determines if the rows are O's"""
                if self.grid[j][i] == "O":
                    O_counter +=1
                    if O_counter == 3:
                        for j in range(3):
                            reprint_x=j*300+150
                            reprint_y=i*300+150
                            txt=gs.Text(gs.Point(reprint_x, reprint_y), "O")
                            txt.setSize(35)
                            txt.setTextColor("red")
                            txt.draw(self.window)  
                        return "O"  
                        """Determines if the right diagonal won"""
        if self.grid[2][0] == self.grid [1][1] == self.grid [0][2]:
            i = 2
            j = 0
            for t in range(3):
                txt=gs.Text(gs.Point(i*300+150, j*300+150), self.grid[2][0])
                txt.setSize(35)
                txt.setTextColor("red")
                txt.draw(self.window)
                i -= 1
                j +=1
            return self.grid[2][0]
            """Determines if the left diagonal won"""
        if self.grid[0][0] == self.grid [1][1] == self.grid [2][2]:
            i=0
            j = 0  
            for i in range(3):
                txt=gs.Text(gs.Point(i*300+150, j*300+150), self.grid[0][0])
                txt.setSize(35)
                txt.setTextColor("red")
                txt.draw(self.window)
                i += 1
                j +=1
            return self.grid[0][0]
        
            """Determines if the game should end and displays text"""
            """If game is at 8 plays remember the last empty coordinate"""
        if game_over == 8:
            self.last_x=0
            self.last_y=0
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):

                    if self.grid[i][j] != "X" and self.grid[i][j] != "O":
                        self.last_x = i
                        self.last_y=j 
        if game_over == 9:            
            return "Draw" 
        return False
        
        
    def end_game(self):
        """Prints Tie game or who winner is"""
        finish = self.isWon() 
        if finish == "Draw":
            txt=gs.Text(gs.Point(450, 350), "Tie Game!")
            txt.setSize(35)
            txt.draw(self.window)
            txt2=gs.Text(gs.Point(self.last_x*300+150, self.last_y*300+150), self.grid[self.last_x][self.last_y])
            txt2.setSize(35)
            txt2.setTextColor("red")
            txt2.draw(self.window)
        else:
            txt=gs.Text(gs.Point(450,350), "Player: " + finish + " Wins!")
            txt.setSize(35)
            txt.draw(self.window)
     
def main():
    game_over = False
    ttt = clickableWindow()
    while game_over == False:
        ttt.window.getMouse()
        game_over = ttt.isWon()
    ttt.end_game()
    ttt.window.getMouse()
main()
