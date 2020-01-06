class Bozo:
	def __init__(self, value):
		print("creating a bozo from:" , value)
		self.value=2*value

	def clown(self, x):
		print ("clowning:" , x)
		print(x*self.value)
		return x + self.value

def main():
	print("clowning aorund now")
	c1 = Bozo(3)
	c2 = Bozo(4)
	print (c1.clown(3))
	#print (c2.clown(c1.clown(2)))

main()