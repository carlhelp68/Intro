class Die:
	def __init__(self, nsides):
		self.nsides = nsides

	def __str__(self):
		return str(self.nsides)

	def __add__(self, another):
		totSides = self.nsides + another.nsides
		return Die(totSides)



def main():
	print("running main in die")
	d = Die(20)
	print(d)
	newd = d + d 
	newd = d.__add__(d)
	print(newd)

if __name__=="__main__":
	main()

	#doesnt work at all