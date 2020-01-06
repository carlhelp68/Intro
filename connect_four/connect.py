import graphics as gs
import random
import time


class clickableWindow:
	def __init__(self, game_mode):
		self.window = gs.GraphWin("Game Sample",690,590)
		self.window.setMouseHandler(self.handleClick)
		self.startScreen()
		self.current_player = 1
		self.over_counter = 0
		self.game_mode = 1
		print(game_mode)
		self.game_mode=game_mode
		print(self.game_mode)

		

	def startScreen(self):
		"""creates board"""



		self.horiz_line= gs.Line(gs.Point(0,100), gs.Point(900, 100))
		self.horiz_line2= gs.Line(gs.Point(0,200), gs.Point(900, 200))
		self.horiz_line3= gs.Line(gs.Point(0,300), gs.Point(900, 300))
		self.horiz_line4= gs.Line(gs.Point(0,400), gs.Point(900, 400))
		self.horiz_line5= gs.Line(gs.Point(0,500), gs.Point(900, 500))
		self.horiz_line6= gs.Line(gs.Point(0,600), gs.Point(900, 600))

		self.vert_line= gs.Line(gs.Point(100,0), gs.Point(100, 900))
		self.vert_line2= gs.Line(gs.Point(200,0), gs.Point(200, 900))
		self.vert_line3= gs.Line(gs.Point(300,0), gs.Point(300, 900))
		self.vert_line4= gs.Line(gs.Point(400,0), gs.Point(400, 900))
		self.vert_line5= gs.Line(gs.Point(500,0), gs.Point(500, 900))
		self.vert_line6= gs.Line(gs.Point(600,0), gs.Point(600, 900))
		self.vert_line7= gs.Line(gs.Point(700,0), gs.Point(700, 900))


	  
		self.horiz_line.draw(self.window)
		self.horiz_line2.draw(self.window)
		self.horiz_line3.draw(self.window)
		self.horiz_line4.draw(self.window)
		self.horiz_line5.draw(self.window)
		self.horiz_line6.draw(self.window)
		
		self.vert_line.draw(self.window)
		self.vert_line2.draw(self.window)
		self.vert_line3.draw(self.window)
		self.vert_line4.draw(self.window)
		self.vert_line5.draw(self.window)
		self.vert_line6.draw(self.window)
		self.vert_line7.draw(self.window)


		self.board_count = [0,0,0,0,0,0,0]
		self.grid = [[],[],[],[],[],[],[]]
		counter = 1
		for x in range(7):
			for y in range(6):
				self.grid[x].append(counter)
				counter+=1
	def handleClick(self, point):
		self.new_x=point.getX()
		self.t = self.new_x//100
		self.H = self.board_count[self.t]
		self.validClick()
		self.board_count[self.t]+=1
		self.grid[self.t][self.H]=self.current_player #getPlayerNum()
		self.setPiece()




		#if self.game_mode == 1:
		if self.current_player ==1:
			self.current_player=-1
		else:
			self.current_player=1



	def getPlayerNum(self):#does nothing right now
		return self.current_player

	def setPiece(self):

		if self.current_player==1:
			piece = gs.Circle(gs.Point(self.new_x//100*100+50, 600-(self.H*100+50)),30)
			piece.setFill('red')
			piece.draw(self.window)
		else:
			piece = gs.Circle(gs.Point((self.new_x//100)*100+50, 600-(self.H*100+50)),30)
			piece.setFill('yellow')
			piece.draw(self.window)
		return piece

	def validClick(self): #doesnt work
		if self.board_count[self.t]>=6:
			print("dingus")

	def isWon(self):
		game_over=False
		for i in range(4):
			for j in range(3):
				self.tileCheck1=self.grid[i][j]
				self.tileCheck2=self.grid[i+1][j+1]
				self.tileCheck3=self.grid[i+2][j+2]
				self.tileCheck4=self.grid[i+3][j+3]
				if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3 and self.tileCheck3==self.tileCheck4:
					return True

		for i in range(7):
			for j in range(3):
				self.tileCheck1=self.grid[i][j]
				self.tileCheck2=self.grid[i][j+1]
				self.tileCheck3=self.grid[i][j+2]
				self.tileCheck4=self.grid[i][j+3]
				if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3 and self.tileCheck3==self.tileCheck4:
					return True
		for i in range(4):
			for j in range(6):
				self.tileCheck1=self.grid[i][j]
				self.tileCheck2=self.grid[i+1][j]
				self.tileCheck3=self.grid[i+2][j]
				self.tileCheck4=self.grid[i+3][j]
				if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3 and self.tileCheck3==self.tileCheck4: 
					return True

		for i in range(3,7):
			for j in range(3):
				self.tileCheck1=self.grid[i][j]
				self.tileCheck2=self.grid[i-1][j+1]
				self.tileCheck3=self.grid[i-2][j+2]
				self.tileCheck4=self.grid[i-3][j+3]
				if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3 and self.tileCheck3==self.tileCheck4:
					return True
		print(self.board_count)
		if self.over_counter==41:
			return True


		self.over_counter+=1
		return False


def computer_turn(self):
	for i in range(4):
			for j in range(3):
				self.tileCheck1=self.grid[i][j]
				self.tileCheck2=self.grid[i+1][j+1]
				self.tileCheck3=self.grid[i+2][j+2]
				if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3:
					piece = gs.Circle(gs.Point((i+3)*100+50, 600-((j+3)*100+50)),30)
					piece.setFill('yellow')
					piece.draw(self.window)


	for i in range(7):
			for j in range(3):
				self.tileCheck1=self.grid[i][j]
				self.tileCheck2=self.grid[i][j+1]
				self.tileCheck3=self.grid[i][j+2]
				if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3:
					piece = gs.Circle(gs.Point((i)*100+50, 600-((j+3)*100+50)),30)
					piece.setFill('yellow')
					piece.draw(self.window)

	for i in range(4):
		for j in range(6):
			self.tileCheck1=self.grid[i][j]
			self.tileCheck2=self.grid[i+1][j]
			self.tileCheck3=self.grid[i+2][j]
			if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3:
				piece = gs.Circle(gs.Point((i+3)*100+50, 600-((j)*100+50)),30)
				piece.setFill('yellow')
				piece.draw(self.window)		
	for i in range(3,7):
		for j in range(3):
			self.tileCheck1=self.grid[i][j]
			self.tileCheck2=self.grid[i-1][j+1]
			self.tileCheck3=self.grid[i-2][j+2]
			if self.tileCheck1==self.tileCheck2 and self.tileCheck2==self.tileCheck3:
				piece = gs.Circle(gs.Point((i-3)*100+50, 600-((j+3)*100+50)),30)
				piece.setFill('yellow')
				piece.draw(self.window)	
















	  
def main():
	game_mode=input("enter 1 or 2")
	game_over = False
	ttt=clickableWindow(game_mode)
	while game_over == False:
		ttt.window.getMouse()
		game_over=ttt.isWon()

	#ttt = startScreen()
main()








