'''Eric Stadelman
Looks for 10001 prime number
5-31-17'''
import math
def isPrime(x):
	'''test every number from 2 to the square root of the number we are testing
	and if any number from 2-square root of x has no remainder its not prime'''
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
			'''if prime returns true'''
			count_prime+=1
	print(count)
main()






		


