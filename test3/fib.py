'''def fib(N):
	if N==0:
		return 0
	if N==1:
		return 1
	return fib(N-1) + fib(N-2)'''



def fib(n):
	if n < 2:
   		return n
	return fib(n-2) + fib(n-1)

def main():
	N=8
	print(fib(N))
main()
