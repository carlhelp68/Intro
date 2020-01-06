class Entry:
	pass

	def __init__(self, name, number):
		self.name=name
		self.number=number

	def number(self):
		return self.number
	def name(self):
		return self.name

def main():
	shannon = Entry("Shannon",634)
	print(shannon.getNumber)
	print(shannon.getNumber())
	shannon.addNumber(35)