'''Eric Stadelman
finds if the sum of the value of the letters equals a triangle value
5-31-17'''
def triangle_values():
	'''creates 100 different t values'''
	list_t=[]
	for t in range(100):
		t_value = (t/2)*(t+1)
		list_t.append(int(t_value))
	return list_t

def triangle_words(list_t,text):
	'''checks to see if the sum of the characters in a word equals a triangle value'''
	value=0
	t_words = 0
	'''removes parenthesis around word'''
	text = [t[1:len(t)-1] for t in text] 
	for word in text:
		for char in word:
			value += (ord(char)-64)
		for i in list_t:
			if i == value:
				t_words+=1
		value = 0
	return t_words

def main():
	inputFile = open("words.txt")
	text = inputFile.read()
	inputFile.close()
	text=text.split(",")
	list_t=triangle_values()
	t_words=triangle_words(list_t,text)
	print(t_words)
main()






