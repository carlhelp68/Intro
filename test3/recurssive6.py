def mystery(L, i =0):
	if i>= len(L):
		return 0
	else:
		result = L[i] + mystery(L,i+2)
		return result
def sum(L):
	sum_values=0
	for i in range(len(L)):
		if i%2==0:
			sum_values+=L[i]
	return sum_values

def main():
	L=[1,2,3,4,6,7,3,5]
	print(sum(L))
	print(mystery(L))
main()



def foo(N):
	if N<1:
		return
	foo(N//2)
	print(N)
def main():
	print(foo(10))
main()