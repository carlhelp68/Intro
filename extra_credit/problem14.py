'''Eric Stadelman     		takes a little over 30 seconds to run!!
looks for the largest sequence of numbers from 1 to one million follow the
collatz algorithm
5-31-17'''
def genSequence(n):
	'''if the n is even divide it by two and if its odd multiply it by 3
	then add 1 and count how many times you can do this until n reaches 1'''
	count = 0
	while n != 1:
		if n%2==0:
			n=n/2
		else:
			n=n*3+1
		count +=1
	return count

def main():
	highest_count = 0
	num = 0
	for i in range(1, 1000000):
		if genSequence(i)>highest_count:
			highest_count=genSequence(i)
			num = i
	print(num)
main()






		


