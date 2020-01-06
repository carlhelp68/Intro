'''Eric Stadelman
Look for largest palindrome number from 2 three digit numbers
5-31-17'''

def palindrome():
	'''intialize variables'''
	value = 0
	string = ""
	highest_value = 0

	'''loop through every multipication possible'''
	for i in range(999):
		for j in range(999):
			value = i * j
			'''turn value into a string so that i can slice it'''
			value = str(value)
			'''slice it from start to finish but going backwards'''
			string = value[::-1]
			'''if the backwards version equals the normal version'''
			if string == value:
				value = int(value)
				if highest_value < value:
					highest_value=value
	return highest_value


def main():
	highest_value = palindrome()
	print(highest_value)
main()