from sys import *
def search(alist, aitem):
	for i in alist:
		if i == aitem:
			return True
	return False
def main():
	list = ["1", 2 ,3 , "t" , 5, 6, 7, 8, 9 ,1, 2,3, 1]
	item = (argv[1])

	t = search(list, item)
	print(t)

main()


#tupile returning something with a comma 

#to switch two lists l[3],l[5] = l[5],l[3]