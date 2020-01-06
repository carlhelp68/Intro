#string = input("Enter your string here: ")
#print(string[2:])


#string = input("Enter your string here: ")
#print("*",string[1:-1] ,"*")

news = ""
news = input("Enter your string here: ")
for c in news:
	if c in ("a e i o u"):
		news = news + ("*")
	else:
		news = news + c
print(news)
