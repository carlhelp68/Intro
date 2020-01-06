import sys
def binSearch(alist, findMe):
		if len(alist)==1:
			if alist[0] == findMe:
				return True
			else:
				return False
		midItem = alist[len(alist)//2]
		if midItem == findMe:
			return True
		elif midItem>findMe:
			return binSearch(alist[:len(alist)//2],findMe)
		else:
			return binSearch(alist[len(alist)//2:], findMe)
def main():
	L = [x*3 for x in range(100)]
	isFound = binSearch(L, int(sys.argv[1]))
	print(isFound)
main()