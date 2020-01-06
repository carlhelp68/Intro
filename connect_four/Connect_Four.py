#Final Project--Connect Four

import turtle
from random import randint
from time import sleep

class ConnectFour:
    def __init__(self):
        '''Constructs the ConnectFour class, requires no parameters'''
        '''creates turtle object and adjusts turtle settings'''
        self.t=turtle.Turtle()
        turtle.tracer(10)
        turtle.setworldcoordinates(0,0,900,800)
        turtle.bgcolor('light grey')
        self.window=turtle.Screen()
        self.t.hideturtle()
        '''instantiates variables'''
        self.turn=1
        self.xClick=0
        self.yClick=0
        self.used=0
        self.tie=False
        self.gameOver=False
        self.gameMode=2

    def mainMenu(self):
        '''Displays the main menu'''
        self.t.up()
        self.t.goto(450,600)
        self.t.color('blue')
        self.t.write("Connect Four!",align='center',font=('Arial',50))
        self.t.goto(450,550)
        self.t.write("By: Ben Gagnon",align='center',font=('Arial',10))
        self.playButton=Button("Play",100,300,self.t)
        self.instructionsButton=Button("Intructions",540,300,self.t)
        self.playButton.draw()
        self.instructionsButton.draw()
        self.window.onscreenclick(self.mainMenuCallback)

    def instructions(self):
        '''Displays the instructions screen'''
        self.window.onscreenclick(self.instructionsCallback)
        self.t.goto(450,650)
        self.t.color('yellow')
        self.t.write("Instructions",align='center',font=('Arial',40))
        self.t.color('black')
        self.t.goto(20,550)
        self.t.write("-    Players will take turns playing pieces on the board",font=('Arial',20))
        self.t.sety(500)
        self.t.write("-    Each piece will drop to the lowest empty space in its column",font=('Arial',20))
        self.t.sety(450)
        self.t.write("-    The first player to connect four pieces in a row wins",font=('Arial',20))
        self.t.sety(400)
        self.t.write("-    A row may be be horizontal, vertical, or diagonal",font=('Arial',20))
        self.t.sety(350)
        self.t.write("-    Have fun!",font=('Arial',20))
        self.mainMenuButton=Button("Menu",320,250,self.t)
        self.mainMenuButton.draw()

    def setup(self):
        '''Gets input from the user to setup the game'''
        self.window.onscreenclick(self.setupCallback)
        self.t.goto(450,650)
        self.t.color('yellow')
        self.t.write("Setup",align='center',font=('Arial',40))
        self.t.color('black')
        self.t.goto(100,550)
        self.t.write("1.  Select game mode",align='left',font=('Arial',20))
        self.t.goto(100,500)
        self.t.write("2.  Enter player name(s) in terminal window",align='left',font=('Arial',20))
        self.singleButton=Button("1 Player",100,300,self.t)
        self.twoButton=Button("2 Player",540,300,self.t)
        self.singleButton.draw()
        self.twoButton.draw()
        
    def play(self):
        '''Starts the game'''
        if self.gameMode==1:
            print ("Player 1")
            self.player1Name=self.getName()
            self.player2Name="Computer"
        else:
            print ("Player 1")
            self.player1Name=self.getName()
            print ("")
            print ("Player 2")
            self.player2Name=self.getName()
        self.board()
        '''binds left mouse event to callback() method'''
        self.window.onscreenclick(self.callback)

    def getName(self):
        '''Gets player name'''
        self.name=input("Enter name: ")
        return self.name
        
    def callback(self,x,y):
        '''Gets the x y values from the left mouse event, calls playerTurn()'''
        self.xClick=x
        self.yClick=y
        self.playerTurn()

    def mainMenuCallback(self,x,y):
        '''Gets the x y values from the left mouse event, interprets them for the main menu'''
        self.xClick=x
        self.yClick=y
        if self.xClick>=100 and self.xClick<=360 and self.yClick>=200 and self.yClick<=300: #play button is clicked
            self.window.onscreenclick(None)
            self.t.clear()
            self.setup()
        if self.xClick>=540 and self.xClick<=800 and self.yClick>=200 and self.yClick<=300: #instructions button is clicked
            self.window.onscreenclick(None)
            self.t.clear()
            self.instructions()

    def instructionsCallback(self,x,y):
        '''Gets the x y values from the left mouse event, interprets them for the instructions menu'''
        self.xClick=x
        self.yClick=y
        if self.xClick>=320 and self.xClick<=580 and self.yClick>=150 and self.yClick<=250:
            self.window.onscreenclick(None)
            self.t.clear()
            self.mainMenu()

    def setupCallback(self,x,y):
        '''Gets the x y values from the left mouse event, interprets them for setup screen'''
        self.xClick=x
        self.yClick=y
        if self.xClick>=100 and self.xClick<=360 and self.yClick>=200 and self.yClick<=300: #Single player button is clicked
            self.window.onscreenclick(None)
            self.gameMode=1
            self.t.clear()
            self.play()
        if self.xClick>=540 and self.xClick<=800 and self.yClick>=200 and self.yClick<=300: #Two player button is clicked
            self.window.onscreenclick(None)
            self.gameMode=2
            self.t.clear()
            self.play()
        
    def board(self):
        '''Creates Tile objects to make up the game board, draws the board'''
        self.gameboard=[]
        for j in range(6): #creates Tile objects and stores them in a two dimensional list
            self.row=[]
            for i in range(7):
                self.x=(i*100)+100
                self.y=(j*100)+100
                tile=Tile(self.x,self.y,self.t)
                self.row.append(tile)
            self.gameboard.append(self.row)
        for row in self.gameboard: #draws the game board
            for tile in row:
                self.t.up()
                tile.draw()
                self.t.up()
        self.columns=["A","B","C","D","E","F","G"]
        for i in range(7): #labels the board columns
            self.t.goto((i*100)+140,710)
            self.t.write(self.columns[i],font=('Arial',20))
        self.t.goto(450,25)
        self.t.color('red')
        self.t.write(self.player1Name+"'s turn!",align='center',font=('Arial',30))
        
    def playerTurn(self):
        '''Alows each player to take their turns'''
        if self.xClick>=100 and self.xClick<=800 and self.yClick>=100 and self.yClick<=700: #checks if player clicked on the board
            self.column=int((self.xClick-100)//100)
            for i in range(len(self.gameboard)): #determines where in selected column player can play
                if self.gameboard[i][self.column].getState()==False:
                    self.row=i
                    self.gameboard[self.row][self.column].picked(self.turn)
                    self.lastPlayerTurn=self.column
                    self.turn=self.turn*-1
                    
                    self.t.goto(0,99) #Updates graphic cues
                    self.t.color('light grey')
                    self.t.down()
                    self.t.begin_fill()
                    for i in range(2):
                        self.t.forward(900)
                        self.t.right(90)
                        self.t.forward(99)
                        self.t.right(90)
                    self.t.end_fill()
                    self.t.up()
                    self.t.goto(450,25)
                    if self.turn==1:
                        self.t.color('red')
                        self.t.write(self.player1Name+"'s turn!",align='center',font=('Arial',30))
                    else:
                        self.t.color('yellow')
                        self.t.write(self.player2Name+"'s turn!",align='center',font=('Arial',30))
                    self.used+=1
                    self.checkWin()
                    break
            if self.gameMode==1 and self.gameOver==False: #starts computer turn in 1 player game
                if self.turn==-1:
                    self.window.onscreenclick(None)
                    self.computerTurn()

    def computerTurn(self):
        '''Plays the computers turn in a 1 player game'''
        self.played=False
        self.avoid=[]
        sleep(1)
        while self.played==False:
            if self.verticalBlock()==True:
                pass
            elif self.horizontalBlock()==True:
                pass
            elif self.diagonalRightBlock()==True:
                pass
            elif self.diagonalLeftBlock()==True:
                pass
            else:
                self.go=False
                while True:
                    self.column=randint(0,6)
                    if self.column not in self.avoid:
                        for i in range(len(self.gameboard)):
                            if self.gameboard[i][self.column].getState()==False:
                                if i>2 and self.gameboard[2][self.column].getPlayerNum()==1:
                                    pass
                                else:
                                    self.go=True
                                    break
                    if self.go==True:
                        break
            for i in range(len(self.gameboard)):
                if self.gameboard[i][self.column].getState()==False:
                    self.row=i
                    self.gameboard[self.row][self.column].picked(self.turn)
                    self.played=True
                    self.turn=self.turn*-1
                    break
                
        self.t.goto(0,99) #updates graphic cues
        self.t.setheading(0)
        self.t.color('light grey')
        self.t.down()
        self.t.begin_fill()
        for i in range(2):
            self.t.forward(900)
            self.t.right(90)
            self.t.forward(99)
            self.t.right(90)
        self.t.end_fill()
        self.t.up()
        self.t.goto(450,25)
        self.t.color('red')
        self.t.write(self.player1Name+"'s turn!",align='center',font=('Arial',30))
        self.window.onscreenclick(self.callback)
        self.checkWin()

    def verticalBlock(self):
        '''Checks to see if the computer can block a vertical win for the player, or make a winning move with a vertical line'''
        self.option=False
        for i in range(7):
            for j in range(3):
                self.tileCheck1=self.gameboard[j][i].getPlayerNum()
                self.tileCheck2=self.gameboard[j+1][i].getPlayerNum()
                self.tileCheck3=self.gameboard[j+2][i].getPlayerNum()
                if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3 and self.tileCheck1!=0:
                    if self.gameboard[j+3][i].getState()==False:
                        self.column=i
                        self.option=True
                        break
        return self.option
            
    def horizontalBlock(self):
        '''Checks to see if the computer can block a horizontal win for the player, or make a winning move with a horizontal line'''
        self.option=False
        for i in range(6):
            for j in range(5):
                self.tileCheck1=self.gameboard[i][j].getPlayerNum()
                self.tileCheck2=self.gameboard[i][j+1].getPlayerNum()
                self.tileCheck3=self.gameboard[i][j+2].getPlayerNum()
                if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3 and self.tileCheck1!=0:
                    if j<=3 and self.gameboard[i][j+3].getState()==False:
                        self.column=j+3
                        if i>=1 and self.gameboard[i-1][self.column].getState()==True:
                            self.option=True
                        elif i==0:
                            self.option=True
                        else:
                            self.avoid.append(self.column)
                        break
                    elif j>=1 and self.gameboard[i][j-1].getState()==False:
                        self.column=j-1
                        if i>=1 and self.gameboard[i-1][self.column].getState()==True:
                            self.option=True
                        elif i==0:
                            self.option=True
                        else:
                            self.avoid.append(self.column)
                        break
                    else:
                        pass
        return self.option

    def diagonalRightBlock(self):
        '''Checks to se if the computer can block a diagonal right win for the player, or make a winning move with a diagonal right line'''
        self.option=False
        for i in range(4):
            for j in range(5):
                self.tileCheck1=self.gameboard[i][j].getPlayerNum()
                self.tileCheck2=self.gameboard[i+1][j+1].getPlayerNum()
                self.tileCheck3=self.gameboard[i+2][j+2].getPlayerNum()
                if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3 and self.tileCheck1!=0:
                    if i<=2 and j<=3 and self.gameboard[i+3][j+3].getState()==False:
                        self.column=j+3
                        if self.gameboard[i+2][self.column].getState()==False:
                            self.avoid.append(self.column)
                        else:
                            self.option=True
                        break
                    elif i>=1 and j>=1 and self.gameboard[i-1][j-1].getState()==False:
                        self.column=j-1
                        if i>=2 and self.gameboard[i-2][self.column].getState()==False:
                            self.avoid.append(self.column)
                        else:
                            self.option=True
                        break
                    else:
                        pass
        return self.option

    def diagonalLeftBlock(self):
        '''Checks to se if the computer can block a diagonal right win for the player, or make a winning move with a diagonal right line'''
        self.option=False
        for i in range(4):
            for j in range(2,7):
                self.tileCheck1=self.gameboard[i][j].getPlayerNum()
                self.tileCheck2=self.gameboard[i+1][j-1].getPlayerNum()
                self.tileCheck3=self.gameboard[i+2][j-2].getPlayerNum()
                if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3 and self.tileCheck1!=0:
                    if i<=2 and j>=3 and self.gameboard[i+3][j-3].getState()==False:
                        self.column=j-3
                        if self.gameboard[i+2][self.column].getState()==False:
                            self.avoid.append(self.column)
                        else:
                            self.option=True
                        break
                    elif i>=1 and j<=6 and self.gameboard[i-1][j-1].getState()==False:
                        self.column=j+1
                        if i>=2 and self.gameboard[i-2][self.column].getState()==False:
                            self.avoid.append(self.column)
                        else:
                            self.option=True
                        break
                    else:
                        pass
        return self.option
        
    def checkWin(self):
        '''Checks to see if ith player has won the game'''
        '''Checks for a horizontal line'''
        for i in range(6):
            for j in range(4):
                self.tileCheck1=self.gameboard[i][j].getPlayerNum()
                self.tileCheck2=self.gameboard[i][j+1].getPlayerNum()
                self.tileCheck3=self.gameboard[i][j+2].getPlayerNum()
                self.tileCheck4=self.gameboard[i][j+3].getPlayerNum()
                if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3 and self.tileCheck3==self.tileCheck4:
                    self.winner=self.tileCheck1
                    if self.winner!=0:
                        self.window.onscreenclick(None)
                        self.gameOver=True
                        self.endGame()
        '''Checks for a vertical line'''
        for i in range(7):
            for j in range(3):
                self.tileCheck1=self.gameboard[j][i].getPlayerNum()
                self.tileCheck2=self.gameboard[j+1][i].getPlayerNum()
                self.tileCheck3=self.gameboard[j+2][i].getPlayerNum()
                self.tileCheck4=self.gameboard[j+3][i].getPlayerNum()
                if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3 and self.tileCheck3==self.tileCheck4:
                    self.winner=self.tileCheck1
                    if self.winner!=0:
                        self.window.onscreenclick(None)
                        self.gameOver=True
                        self.endGame()
        '''Checks for a diagonal line to the right'''
        for i in range(3):
            for j in range(4):
                self.tileCheck1=self.gameboard[i][j].getPlayerNum()
                self.tileCheck2=self.gameboard[i+1][j+1].getPlayerNum()
                self.tileCheck3=self.gameboard[i+2][j+2].getPlayerNum()
                self.tileCheck4=self.gameboard[i+3][j+3].getPlayerNum()
                if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3 and self.tileCheck3==self.tileCheck4:
                    self.winner=self.tileCheck1
                    if self.winner!=0:
                        self.window.onscreenclick(None)
                        self.gameOver=True
                        self.endGame()
        '''Checks for a diagonal line to the left'''
        for i in range(3):
            for j in range(3,7):
                self.tileCheck1=self.gameboard[i][j].getPlayerNum()
                self.tileCheck2=self.gameboard[i+1][j-1].getPlayerNum()
                self.tileCheck3=self.gameboard[i+2][j-2].getPlayerNum()
                self.tileCheck4=self.gameboard[i+3][j-3].getPlayerNum()
                if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3 and self.tileCheck3==self.tileCheck4:
                    self.winner=self.tileCheck1
                    if self.winner!=0:
                        self.window.onscreenclick(None)
                        self.gameOver=True
                        self.endGame()
        '''Checks for a tie'''
        if self.used==42:
            self.tie=True
            self.gameOver=True
            self.onscreenclick(None)
            self.endGame()
            
    def endGame(self):
        '''Game is over, announces winner'''
        print ("")
        print ("Game Over!")
        self.t.goto(0,99)
        self.t.color('light grey')
        self.t.down()
        self.t.begin_fill()
        for i in range(2):
            self.t.forward(900)
            self.t.right(90)
            self.t.forward(99)
            self.t.right(90)
        self.t.end_fill()
        self.t.up()
        if self.winner==1:
            print (self.player1Name,"wins!")
            self.t.goto(450,25)
            self.t.color('red')
            self.t.write(self.player1Name+" wins!",align='center',font=('Arial',30))
        elif self.tie==True:
            print ("Tie!")
            self.t.goto(450,25)
            self.t.color('blue')
            self.t.write("Tie!",align='center',font=('Arial',30))
        else:
            print (self.player2Name,"wins!")
            self.t.goto(450,25)
            self.t.color('yellow')
            self.t.write(self.player2Name+" wins!",align='center',font=('Arial',30))
        sleep(2)
        turtle.bye()

class Tile:
    def __init__(self,x,y,t):
        '''Constructs the Tile object, takes x y position and turtle object as parameters'''
        '''instantiates variables'''
        self.x=x
        self.y=y
        self.t=t
        self.used=False
        self.playerNum=0
        
    def draw(self):
        '''Draws the Tile object in the turtle window'''
        self.t.goto(self.x,self.y)
        self.t.down()
        self.t.setheading(360)
        self.t.color('blue')
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(100)
            self.t.left(90)
        self.t.end_fill()
        self.t.goto(self.x+50,self.y+10)
        self.t.color('white')
        self.t.begin_fill()
        self.t.circle(40)
        self.t.end_fill()
        self.t.up()
        
    def picked(self,playerNum):
        '''Called when the Tile object is played on'''
        self.playerNum=playerNum
        self.t.up()
        if self.playerNum==1:#if Tile object is played on by first player
            self.used=True
            self.t.color('red')
            self.t.goto(self.x+50,self.y+10)
            self.t.begin_fill()
            self.t.circle(40)
            self.t.end_fill()
        else:#if Tile object is played on by second player
            self.used=True
            self.t.color('yellow')
            self.t.goto(self.x+50,self.y+10)
            self.t.begin_fill()
            self.t.circle(40)
            self.t.end_fill()
            
    def getState(self):
        '''Returns state of Tile object (used/unused)'''
        return self.used
    
    def getPlayerNum(self):
        '''Returns the number of player that has played on the Tile object'''
        return self.playerNum

class Button:
    def __init__(self,text,x,y,t):
        '''Constructs the Button class, takes text, x y coordinates and a turtle object as parameters'''
        self.text=text
        self.x=x
        self.y=y
        self.t=t

    def draw(self):
        '''Draws the button object'''
        self.t.goto(self.x,self.y)
        self.t.setheading(0)
        self.t.begin_fill()
        self.t.color('red')
        for i in range(2):
            self.t.forward(260)
            self.t.right(90)
            self.t.forward(100)
            self.t.right(90)
        self.t.end_fill()
        self.t.up()
        self.t.goto(self.x+130,self.y-80)
        self.t.color('black')
        self.t.write(self.text,align='center',font=('Arial',35))
        
def main():
    '''Gets player names and creates a ConnectFour object'''
    print ("Connect Four!")
    print ("")
    game=ConnectFour()
    game.mainMenu()
    turtle.mainloop()

main()
        
