import pygame
import random


class game:
	def __init__(self, screen, color):
		self.inplay= True
		self.playscore1 = 0
		self.playscore2 = 0
		self.screen = screen
		self.screen_color = color
		self.ball = Ball(10, 10, "red", (400, 300), 2, 800, 400)
		self.paddle1 = Paddle(40, 3, "blue", 20, (3,200), 400 )
		self.paddle2 = Paddle(40, 3, "blue", 20, (797,200), 400)
		pygame.display.set_caption("Player one's score is " + str(self.playscore1) + \
					" Player two's score is " + str(self.playscore2))

	def play(self):
		playscore1= 0
		playscore2= 0
		print(self.inplay)
		while self.inplay and playscore2 <10 and playscore1<10:
			events = pygame.event.get()
			for event in events:
				self.handleEvent(event)
			#if self.ball is in range of x and y, dont change directoin
			# if self.ball.pos[0] > 1 and self.ball.pos[0] < 799 \
			# and self.ball.pos[1] > 0 and self.ball.pos[1] < 400:

				#print(self.ball.pos)
			
			#check if ball hits paddle1
			if self.ball.pos[0] == self.paddle1.pos[0] + self.paddle1.width:
				if self.ball.pos[1] > self.paddle1.pos[1] - .25*self.paddle1.length:
					if self.ball.pos[1] < self.paddle1.pos[1] + self.paddle1.length:
						self.ball.dir[0] *= -1 #reverse direction of ball
						self.ball.dir[1] = random.uniform(-1,1)
			#check if ball hits paddle2
			if self.ball.pos[0] == self.paddle2.pos[0] - self.paddle2.width:
				if self.ball.pos[1] > self.paddle2.pos[1] - .25*self.paddle2.length:
					if self.ball.pos[1] < self.paddle2.pos[1] +self.paddle2.length:
						self.ball.dir[0] *= -1 #reverse direction of ball
						self.ball.dir[1] = random.uniform(-1,1)

			#check if ball hits top or bottom boundary	
			if self.ball.pos[1] <= 0 or self.ball.pos[1] >= 400:
				print("should be reversing direction")
				self.ball.dir[1]*= -1

			#check if ball got past paddle1
			if self.ball.pos[0]== 0:
				self.playscore2 += 1
				self.ball.pos = [400, 200]
				pygame.display.set_caption("Player one's score is " + str(self.playscore1) + \
					" Player two's score is " + str(self.playscore2))
				#reset ball to the middle

			#check if ball got past paddle2
			if self.ball.pos[0]== 800:
				self.playscore1 += 1
				self.ball.pos = [400, 200]
				pygame.display.set_caption("Player one's score is " + str(self.playscore1) + \
					" Player two's score is " + str(self.playscore2))
				#reset ball to middle
					
			self.ball.moveStep()
			self.draw()
			#movePaddle(self)
				#print(self.ball.pos)
				

				#reset
			

	def handleEvent(self,event):
		if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			if self.paddle2.pos[1] + self.paddle2.length > 0:
				self.paddle2.pos[1] -= 20
		if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			if self.paddle2.pos[1] + self.paddle2.length < 399:
				self.paddle2.pos[1] += 20
		if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			if self.paddle1.pos[1] + self.paddle1.length > 0:
				self.paddle1.pos[1] -= 20
		if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			if self.paddle1.pos[1] + self.paddle1.length < 399:
				self.paddle1.pos[1] += 20


			#if 0<self.paddle1.pos[0] < 399:
	
			# 	if (pygame.key.get_pressed()[pygame.K_w]):
			# 		self.paddle1.pos[0]+= 10
			# 	if (pygame.key.get_pressed()[pygame.K_s]):
			# 		self.pos[0] -= 10

			# if 0<self.paddle2.pos[0] < 399:	
			# 	if (pygame.key.get_pressed()[pygame.K_UP]):
			# 		self.paddle2.pos[0]+= 10
			# 	if (pygame.key.get_pressed()[pygame.K_DOWN]):
			# 		self.paddle2.pos[0] -= 10
	
		#draw ball and both paddles here
	def draw(self):
		#draw first paddle
		self.screen.fill(self.screen_color)
		pygame.draw.rect(self.screen, (255,0,0), [self.paddle1.pos[0], self.paddle1.pos[1], self.paddle1.width, self.paddle1.length])
		#draw ball
		pygame.draw.rect(self.screen, (0,255,0),  [self.ball.pos[0], self.ball.pos[1], self.ball.radius/2, self.ball.radius/2])

		#draw second paddle minus eight only there for aesthetics
		pygame.draw.rect(self.screen, (0,0,255), [self.paddle2.pos[0],self.paddle2.pos[1],self.paddle2.width, self.paddle2.length])
		pygame.display.flip()

	def movePaddle(self):
		def __init__(self, length, color, speed, initPos, boundsY):
			#Make an instance and repeat checks for AS
			if 0<self.paddle1.pos[0] < 399:
	
				if (pygame.key.get_pressed()[pygame.K_w]):
					self.paddle1.pos[0]+= 10
				if (pygame.key.get_pressed()[pygame.K_s]):
					self.pos[0] -= 10

			if 0<self.paddle2.pos[0] < 399:	
				if (pygame.key.get_pressed()[pygame.K_UP]):
					self.paddle2.pos[0]+= 10
				if (pygame.key.get_pressed()[pygame.K_DOWN]):
					self.paddle2.pos[0] -= 10


		def getPos(self):
			return self.pos






#class Pong:
#	def makeBoard(self):
		
#		pygame.display.init()
#		self.screen=pygame.display.set_mode((800,400))
		
class Paddle:
	def __init__(self, length, width, color, speed, initPos, boundsY):
		self.length= length
		self.width = width
		self.color = color
		self.speed = speed
		self.pos = list(initPos)
		self.boundsY = boundsY
		#self.keyup = keyup
		#self.keydown = keydown

	def getPos(self):
		print(self.pos)
		return self.pos

class Ball:
	def __init__(self, radius, sideLength, color, initPos, speed, boundsX, boundsY):
		self.radius = radius
		self.pos = list(initPos)
		self.sideLength = sideLength
		self.color = color
		self.speed = speed
		#make a vector for dir that changes
		self.dir= [1,0]
		self.boundsX = boundsX
		self.boundsY = boundsY

	#def draw(self, screen):
		#pygame.draw(screen, self.color, self.pos[0],self.pos[1],self.sidelength, self.sidelength)

	def moveStep(self):
		#move ball in the current direction with a set speed
		self.pos[0] += self.dir[0]*self.speed
		self.pos[1] += self.dir[1]*self.speed

	def getSideLength(self):
		return self.sideLength

	def getPos(self):
		print(self.pos)
		return self.pos


	def changeColor(self):
		self.color = "red"
def main():

	windimensions = 100,100
	window = pygame.display.set_mode(windimensions)
	pygame.display.set_caption("Instruction Window")
	instructions = ["Left paddle click 'W' for up, and 'S' for down, Right paddle click UP ARROW for up and DOWN ARROW for down"]
	myfont = pygame.font.SysFont("Cambria", 22)
	instrline1 = myfont.render(instructions[1],1,(75,0,75))
	instrline2 = myfont.render(instructions[2],1,(75,0,75))
	window.blit(instrline1, (50,100))
	window.blit(instrline2, (50,100))
	pygame.display.flip()



	# sets up all pygame modules for use
	pygame.init()
	# set up window with given width, height, and caption
	winWidth, winHeight = 800, 400
	screen = pygame.display.set_mode([winWidth, winHeight])
	


	# initialize parameters and draw just background screen
	running = 1
	bgcolor = (0,0,0)
	screen.fill(bgcolor)
	pygame.display.flip()
	game_object = game(screen, bgcolor)
	# game_object.moveStep()

	game_object.draw()
	game_object.play()







main()
