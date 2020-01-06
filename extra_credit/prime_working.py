import math


def isPrime(x):
	for i in range(2, int(math.sqrt(x)+1)):
		if x%i==0:
			return False
	return True


def main():
	count = 1
	count_prime=0
	while count_prime<10001:
		count+=1
		if isPrime(count):
			count_prime+=1
			print(str(count_prime),str(count))
		
		
	print(count)
main()






		


