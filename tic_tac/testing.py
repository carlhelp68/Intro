#set text in box
#alternate player turns
#check to see if valid
#isWon

import graphics as gs
import random
import time


class TicTacToe:
	def __init__(self):
		self.window = gs.GraphWin("Game Sample",900,900)
		self.window.setMouseHandler(self.handleClick)
		self.startScreen()
		self.currentplayer = "X" 
		self.grid =[[1,2,3],[4,5,6],[7,8,9]] 

	def startScreen(self):
		self.horiz_line= gs.Line(gs.Point(0,300), gs.Point(900, 300))
		self.horiz_line2= gs.Line(gs.Point(0,600), gs.Point(900, 600))
		self.vert_line= gs.Line(gs.Point(300,0), gs.Point(300, 900))
		self.vert_line2= gs.Line(gs.Point(600,0), gs.Point(600, 900))
		self.horiz_line.draw(self.window)
		self.horiz_line2.draw(self.window)
		self.vert_line.draw(self.window)
		self.vert_line2.draw(self.window)
		self.grid = []
		self.clicks = []
			
	def handleClick(self, point):
		count = 0
		if count%2 == 0:
			#self.currentplayer = "X"
			new_x=point.getX()
			new_y=point.getY()
			self.grid[new_x//300:new_y//300] = "X"
			count += 1
		else:
			new_x=point.getX()
			new_y=point.getY()
			self.grid[new_x//300:new_y//300] = "O"
			count+= 1

		#self.grid[new_x//300][new_y//300] =	 self.currentplayer
		print(self.grid)
	

	def playerXturn(self):
		self.currentplayer = "X"
		self.window.setMouseHandler(self.handleClick)
			
			
		#if click is in one of nine boxes
			#set variable equal to middle of box that was clicked
			#use variable and call on setText with middle of box saved
			#how to deal with player either x or O 

	def playerYturn(self):
		self.currentplayer = "O"
		self.window.setMouseHandler(self.handleClick)
			
			

	def setText(self,txt):
		if count%2 == 0:
			txt=Text(Point(new_x + 450, new_y + 450), "X")
		else:	
			txt=Text(Point(new_x + 450, new_y + 450), "O")

		return txt
			#set text to where ever the middle of the box is saved 
			
		
def main():
	ttt = TicTacToe()
	ttt.startScreen()
	ttt.playerXturn()
	#ttt.setText()
	print("here")
	ttt.playerYturn()
	input("here")
	#ttt.setText()
	
main()
