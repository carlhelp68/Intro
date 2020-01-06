import math
x = input("Enter number here >")
x = int(x)
if x == 0:
	print("Cant handle 0")
else:
	isPrime = True
	for i in range(2, int(math.sqrt(x)+1)):
		if x%i==0:
			print("Not prime")
			isPrime = False
			break
		if isPrime==True:
			print("Prime")
			break