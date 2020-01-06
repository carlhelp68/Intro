def listaddone(list,x):
	for i in range(0,len(list)):
		#if L(i)==i:
		list[i] += x
	return list



def main():
	x = input("Please enter number here:")
	x = int(x)
	list=[1,3,4,5]
	newL = listaddone(list, x)
	print(newL)
	print(list)
main()