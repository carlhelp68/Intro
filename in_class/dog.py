class dogs:
	def __init__(self, name="dog", breed = "bulldog" , happiness =4):
		self.name = name
		self.breed=breed
		self.happiness =happiness

	def giveTreats(self, numTreats=5):
		self.happiness +=numTreats
		if self.happiness>10:
			self.happiness=10
	def __str__(self):
		return self.name + " " + self.happiness
def main():
	mydog1 = dogs("5")
	mydog1.giveTreats()
	#print(type(mydog1.breed))
	#print(mydog1.name)
	#print(type(mydog1.happiness))
	print(some_dog)
main()