def printMessage(text,number):
	if number==0:
		return True
	print("here")
	printMessage(text, number-1)
	print(text)
	
def main():
	number = 5
	text = "hello"
	ttt=printMessage(text, number)
	print(ttt)
main()