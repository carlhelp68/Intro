inputFile = open("words.txt")
text = inputFile.read()
inputFile.close()
list=[]
t_value = 0
value=0
list_ord=[]
t_words = 0
text=text.split(",")

for t in range(100):
	t_value = (t/2)*(t+1)
	list.append(int(t_value))

for i in range(len(text)):
	text[i] = text[i][1:len(text[i])-1]

	for j in range(len(text[i])):
		value += (ord(text[i][j])-64)
	for i in list:
		if i == value:
			t_words+=1
	value=0
print(t_words)






