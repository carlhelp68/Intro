s = input("Enter a string: ")
#found = False
x = input("Enter a character here: ")
t = 0


frequency = []
times_counted = 0
alphabet_value = 97



for c in s:	
	if c==x:
		t = t +1
		#print("Found your character" ,c)
		#found = True
		#break
print(t)
frequency.append(t)
print(frequency)
#if not found:
#	print("not found")
#	found = False


