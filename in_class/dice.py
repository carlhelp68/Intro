import random

class Die:
		def __init__(self, nSides):
			self.numSides = nSides
			self.color = (250,0,0)

		def display(self):
			print("numSides=" , self.numSides)
			print("Color=" , self.color)

		def getSides(self):
			return self.numSides

		def setSides(self, newSides):
			self.numSides=newSides
		
		def roll(self):
			print(random.randint(1, self.numSides))



def main():
		myDie = Die(20)
		die2 = Die(6)

		myDie.setSides(8)

		print("numsides=" , myDie.getSides())

		#myDie.display()
		#die2.display()

		myDie.roll()
		die2.roll()
main()