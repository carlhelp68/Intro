'''Eric Stadelman
this program plays connect 4 between either two humans or between 1 person
and the AI
6-5-17'''


import graphics as gs
import random

class clickableWindow:
	def __init__(self, game_mode):
		self.game_mode=game_mode
		self.window = gs.GraphWin("Connect Four!",690,590)
		self.window2=gs.GraphWin("Game Rules!" , 520, 320)
		self.window.setMouseHandler(self.handleClick)
		self.startScreen()
		if self.game_mode ==1:
			self.current_player = 1
		if self.game_mode == 2:
			self.current_player = -1
		self.over_counter = 0

		

	def startScreen(self):
		"""creates board with large blue rectangle and draws white circles over
		also creates lines to show columns and rows and intializes the board count
		which tells how many pieces are in each column and grid which are cordinates
		showing which spots are taken by filling with a 1 or -1"""

		self.back_ground=gs.Rectangle(gs.Point(0,0), gs.Point(690,590))
		self.back_ground.setFill('blue')
		self.back_ground.draw(self.window)
		for i in range(7):
			for j in range(6):
				self.Circle=gs.Circle(gs.Point(i*100+50,j*100+50),(30))
				self.Circle.setFill('white')
				self.Circle.draw(self.window)

		for i in range(6):
			'''creates lines'''
			self.horiz_line= gs.Line(gs.Point(0,i*100+100), gs.Point(900, i*100+100))
			self.vert_line= gs.Line(gs.Point(100*i+100,0), gs.Point(100*i+100, 900))

			self.horiz_line.draw(self.window)
			self.vert_line.draw(self.window)

		self.board_count = [0,0,0,0,0,0,0]
		self.grid = [[],[],[],[],[],[],[]]
		counter = 2
		'''creates game grid'''
		for x in range(7):
			for y in range(6):
				self.grid[x].append(counter)
				counter+=1
		'''prints rules to a seperate window'''
		rule1=gs.Text(gs.Point(260,100), "The goal of the game is to get 4 in a row!")
		rule1.setFill('green')
		rule1.setSize(20)
		rule1.draw(self.window2)

		rule2=gs.Text(gs.Point(260,130), "Players alternate every turn until game is over!")
		rule2.setFill('green')
		rule2.setSize(20)
		rule2.draw(self.window2)

		rule3=gs.Text(gs.Point(260,160), "4 pieces in a row vertically, diagnolly, or horizontally win!")
		rule3.setFill('green')
		rule3.setSize(20)
		rule3.draw(self.window2)

		rule4=gs.Text(gs.Point(260,190), "The first person to get 4 in any of those directions wins!")
		rule4.setFill('green')
		rule4.setSize(20)
		rule4.draw(self.window2)

		rule5=gs.Text(gs.Point(260,220), "Any left click in a column should be so long as it is not full!")
		rule5.setFill('green')
		rule5.setSize(20)
		rule5.draw(self.window2)


			
	def handleClick(self, point):
		'''handles click and puts it into board count and grid for user input
		and calls on set piece'''

		'''takes clicks x cordinate and does integer division by 100 to put it
		coordinates and then adds it to the board count and grid'''
		self.new_x=point.getX()
		self.x = self.new_x//100
		self.y = self.board_count[self.x]
		if self.valid_human_click(self.x):
			self.over_counter+=1
			self.board_count[self.x]+=1
			self.grid[self.x][self.y]=self.current_player
			
			'''if a two player game swithc between the two players'''
			if self.game_mode == 2:
				if self.current_player ==1:
					self.current_player=-1
				else:
					self.current_player=1
					'''if single player game call on the computers turn'''
			if self.game_mode == 1: #help with puesdo code from Adi the prefect
				if self.isWon()==False:
					self.over_counter+=1
					self.computer_turn()


			self.setPiece()


	def valid_human_click(self, x):
		'''checks to see if human click is valid by seeing if the column has less
		than 6 pieces in it'''
		if self.board_count[x]>=6:
			print("Invalid Click!")
			return False
		else:
			return True

	def setPiece(self):
		'''draws pieces to the board depending if it player one or two and the
		current player. takes coordinates multiplies them by 100 to put them in
		the proper square and then adds 50 to center the piece'''
		if self.current_player==1:
			piece = gs.Circle(gs.Point(self.x*100+50, 600-(self.y*100+50)),30)
			piece.setFill('red')
			piece.draw(self.window)
		else:
			piece = gs.Circle(gs.Point(self.x*100+50, 600-(self.y*100+50)),30)
			piece.setFill('yellow')
			piece.draw(self.window)
		return


	def isWon(self):
		'''to check if there are any winners, returns true if there are
		and calls print winner function, returns false if no winners'''
		game_over=False
		'''checks to see if there is a right diagnal winner'''
		for i in range(4): #help from Ben Gagnon on puesdo code with win checks
			for j in range(3):
				self.square1=self.grid[i][j]
				self.square2=self.grid[i+1][j+1]
				self.square3=self.grid[i+2][j+2]
				self.square4=self.grid[i+3][j+3]
				if self.square1==self.square2 and self.square2==self.square3 and self.square3==self.square4:
					self.print_winner(self.square1)
					return True
		'''checks to see if there is a vertical winner'''
		for i in range(7):
			for j in range(3):
				self.square1=self.grid[i][j]
				self.square2=self.grid[i][j+1]
				self.square3=self.grid[i][j+2]
				self.square4=self.grid[i][j+3]
				if self.square1==self.square2 and self.square2==self.square3 and self.square3==self.square4:
					self.print_winner(self.square1)
					return True
		'''checks to see if horizontal has won'''
		for i in range(4):
			for j in range(6):
				self.square1=self.grid[i][j]
				self.square2=self.grid[i+1][j]
				self.square3=self.grid[i+2][j]
				self.square4=self.grid[i+3][j]
				if self.square1==self.square2 and self.square2==self.square3 and self.square3==self.square4: 
					self.print_winner(self.square1)
					return True
		'''checks for left diagnal winner'''
		for i in range(3,7):
			for j in range(3):
				self.square1=self.grid[i][j]
				self.square2=self.grid[i-1][j+1]
				self.square3=self.grid[i-2][j+2]
				self.square4=self.grid[i-3][j+3]
				if self.square1==self.square2 and self.square2==self.square3 and self.square3==self.square4:
					self.print_winner(self.square1)
					return True
		'''if 42 moves have been played on the board and a winner was not detected
		it is a tie game'''
		if self.over_counter==42:
			self.print_winner(3)
			return True
		return False

	def print_winner(self, winner):
		'''prints whoever the winner is or if its tie game'''
		'''if winner equals three that means 42 moves have been played on the board
		and no winner is detected prints tie game'''
		if winner == 3:
			txt=gs.Text(gs.Point(345,300), "Tie Game!")
			txt.setFill('white')
			txt.setSize(35)
			txt.draw(self.window)
			return
		'''if it is a two player game and the winner is -1 first player has won 
		(usually -1 is player two but they are switched before going into the iswin
		function)'''
		if self.game_mode == 2:
			if winner == -1:
				txt=gs.Text(gs.Point(345,300), "First Player Won!")
				txt.setFill('white')
				txt.setSize(35)
				txt.draw(self.window)
				return
			'''' if winner equals one second player has won 
			(again because they switch prior to the isWon function)'''
			if winner == 1:
				txt=gs.Text(gs.Point(345,300), "Second Player Won!")
				txt.setFill('white')
				txt.setSize(35)
				txt.draw(self.window)
				return
				'''if game mode equals one player either you won or computer won 
				will be printed'''		
		else:
			if winner == 1:
				txt=gs.Text(gs.Point(345,300), "You Won!")
				txt.setFill('white')
				txt.setSize(35)
				txt.draw(self.window)
				return
			else:
				txt=gs.Text(gs.Point(345,300), "Computer Won!")
				txt.setFill('white')
				txt.setSize(35)
				txt.draw(self.window)
				return

	'''checks if the piece the computer is going to place is valid'''
	def valid_piece(self, x, y):
		'''if it tries to place it higher than the highest piece'''
		if self.board_count[x]>y:
			return False
		''' if it tries to place below the highest piece'''
		if self.board_count[x]<y:
			return False
		'''if it tries to place it in a column with 6 pieces already'''
		if self.board_count[x]>=6:
			return False
		else:
			return True
		
	
	def draw_computer(self, x ,y):
		'''draws computer piece and adds it to board count and game grid'''
		'''the reason for x * 100 +50 and the same for y is because they are
		cordinates from the game grid so they need to be multiplied and centered
		when drawn'''
		piece = gs.Circle(gs.Point((x)*100+50, 600-((y)*100+50)),30)
		piece.setFill('yellow')
		piece.draw(self.window)
		self.board_count[x]+=1
		self.grid[x][y] =-1
		return

	def computer_turn(self):
		'''AI: computer checks if there are three in a row of either color or two
		in a row of either color and adds to those if there is. for example if there
		are 3 reds vertically the computer will place on top of those three
		uses same checks as the isWon but only looks for 2 or 3 in a row'''
		'''checks if diagnol right has 4 in a row and places piece if '''
		for i in range(4):
			for j in range(3):
				self.square1=self.grid[i][j]
				self.square2=self.grid[i+1][j+1]
				self.square3=self.grid[i+2][j+2]
				if self.square1==self.square2 and self.square2==self.square3:
					if self.valid_piece(i+3, j+3):
						self.draw_computer(i+3,j+3)
						return
					if self.valid_piece(i-1, j-1):
						self.draw_computer(i-1,j-1)

					else:
						self.random_turn()
						return

		'''checks to see if there are three vertical pieces in a row'''
		for i in range(7):
			for j in range(3):
				self.square1=self.grid[i][j]
				self.square2=self.grid[i][j+1]
				self.square3=self.grid[i][j+2]
				if self.square1==self.square2 and self.square2==self.square3:
					if self.valid_piece(i,j+3):
						self.draw_computer(i, j +3)
						return
					else:
						self.random_turn()
						return

		'''checks to see if three pieces are in a row horizontally and places
		to the left or right of it'''
		for i in range(4):
			for j in range(6):
				self.square1=self.grid[i][j]
				self.square2=self.grid[i+1][j]
				self.square3=self.grid[i+2][j]
				if self.square1==self.square2 and self.square2==self.square3:
					if self.valid_piece(i+3,j):
						self.draw_computer(i+3,j)
						return
					if self.valid_piece(i-1,j):
						self.draw_computer(i-1,j)
						return
					else:
						self.random_turn()
						return
				
		'''checks to see if there are three in a row in a left diagnol'''		
		for i in range(3,7):
			for j in range(3):
				self.square1=self.grid[i][j]
				self.square2=self.grid[i-1][j+1]
				self.square3=self.grid[i-2][j+2]
				if self.square1==self.square2 and self.square2==self.square3:
					if self.valid_piece(i-3,j+3):
						self.draw_computer(i-3,j+3)
						return
					if self.valid_piece(i+1, j-1):
						self.draw_computer(i+1,j-1)
					else:
						self.random_turn()
						return
		'''checks to see if there are two in a right diagnol'''
		for i in range(4):
			for j in range(3):
				self.square1=self.grid[i][j]
				self.square2=self.grid[i+1][j+1]
				if self.square1==self.square2:
					if self.valid_piece(i+2, j+2):
						self.draw_computer(i+2,j+2)
						return
					if self.valid_piece(i-1, j-1):
						self.draw_computer(i-1,j-1)
					else:
						self.random_turn()
						return
		'''checks to see if there are two vertically'''
		for i in range(7):
			for j in range(3):
				self.square1=self.grid[i][j]
				self.square2=self.grid[i][j+1]
				if self.square1==self.square2:
					if self.valid_piece(i,j+2):
						self.draw_computer(i, j +2)
						return
					if self.valid_piece(i,j-1):
						self.draw_computer(i, j -1)
						return
					else:
						self.random_turn()
						return
		'''hecks to see if there are two horizontally'''
		for i in range(4):
			for j in range(6):
				self.square1=self.grid[i][j]
				self.square2=self.grid[i+1][j]
				if self.square1==self.square2:
					if self.valid_piece(i+2,j):
						self.draw_computer(i+2,j)
						return
					if self.valid_piece(i-1,j):
						self.draw_computer(i-1,j)
						return
					else:
						self.random_turn()
						return
		'''checks to see if there are two in a left diagnol'''		
		for i in range(3,7):
			for j in range(3):
				self.square1=self.grid[i][j]
				self.square2=self.grid[i-1][j+1]
				if self.square1==self.square2:
					if self.valid_piece(i-2,j+2):
						self.draw_computer(i-2,j+2)
						return
					if self.valid_piece(i+1, j-1):
						self.draw_computer(i+1,j-1)
					else:
						self.random_turn()
						return
						'''if non of the prior worked, pick a random but valid spot'''
		else:
			self.random_turn()

	def random_turn(self):
		'''picks a random spot to put it, checks if its valid
		if it is it calls the computer draw function and if it isnt
		it recycles through until it picks a valid spot'''
		i = random.randint(0,6)
		j = random.randint(0,7)
		if self.valid_piece(i, j):
			self.draw_computer(i, j)
			return
		else:
			self.random_turn()	
	def dummy_click_handler(self, point): #help from cousin Cam, CS major
		'''this handles clicks after the game is over but the user has not quit
		from the terminal nothing = "nothing is simply there so that it can compile'''
		nothing = "nothing" 

def main():
	'''asks for how many players, if 1 or 2 is not entered single player game
	is initiated'''

	'''to handle any input besides a 1 or a 2, 1 player will be played if 
	incorrect input''' #Help from Sherri during office hours
	game_mode=input("How many players? enter 1 or 2 ")
	if len(game_mode) !=1 or game_mode.isdigit() == False and game_mode != "1" or game_mode !="2":
		game_mode =1
		game_mode = int(game_mode)

	else:
		game_mode = int(game_mode)
	game_over = False
	connect=clickableWindow(game_mode)
	while game_over == False:
		connect.window.getMouse()
		game_over=connect.isWon()
	connect.window.setMouseHandler(connect.dummy_click_handler)
	input("Hit enter to quit")
main()








