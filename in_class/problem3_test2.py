def addItem(aList, aVal):
    aVal += 1
    aList.append(aVal)
    return(aVal)
def main():
	L = [1,2,3,4]
	x= 6
	t = 2
	y = addItem(L, t)
	print (L)
	print (x)
	print (y)
main()