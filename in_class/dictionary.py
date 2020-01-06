def addname(D):
	name=input("Enter name here:")
	number=int(input("Enter number here:"))
	D[name] = number
	return D

def findname(D):
	name2=input("Enter name here:")
	for i in range(D):
		if name == i:
			print(number2)
			#return i:
		else:
			print("not found")

def main():
	D=dict()
	addname(D)
	findname(D)
	print(D)
	print(number2)

main()




pb = {"sherri" : [65]}
pb["shannon"] = [33]
listOfNumbers = pb["shannon"]
listOfNumbers.append(22)
pb["shannon"].append(11)
print(pb)





class Entry:
	pass
def main():
	shannon = Entry("Shannon",634)
	print(shannon.getNumber())
	shannon.addNumber(35)


	