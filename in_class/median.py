values = input("Enter value here")
values = int(values)
list = []
count = 0
x=1


while x==1:
	if values == -1:
			list.sort()
			print(list[int(count/2)])
			x = x-1

	else:
		list.append(values)
		count = count +1
		values = input("Enter value here")
	
	
	
		