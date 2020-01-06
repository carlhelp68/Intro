'''Eric Stadelman
multiplies the sum all the values of the letters in a name and then
multilies by the posistion in the list
5-31-17'''
def get_score(name):
	'''makes all letters undercase and the gets the ASCII values then subtracts
	96 so that a = 1 and then sums all the letter values for a name'''
	name_score = 0
	for i in name.lower():
		name_score += ord(i) - 96
	return name_score

def main():
	'''opens the names file and splits it into a list and then replaces all the
	quotations at the start and end of the name with a blank spot the sorts the names'''
	names_file = open("names.txt", 'r')
	names = names_file.read().split(',')
	'''remmoves parenthesis around word'''
	names = [n.replace('"', '') for n in names]
	names.sort()
	total_score = 0
	for i in range(0, len(names)):
		'''takes the value of all the letters and then multiplies by its index +1 
		in the list spot and sums them all together'''
		total_score += (i+1) * get_score(names[i])
	print(total_score)
main()