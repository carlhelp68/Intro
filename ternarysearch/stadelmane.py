"""Eric Stadelman
This program searches for an item in a list by either slicing it or changing
the window size it looks through
5-29-17"""
import sys
import time
def terSearch(alist, aterm):
	"""this function slices the program depending if the item were looking for is
	bigger or smaller than the 1/3 item through the list and the 2/3 item through
	the list"""

	"""Base cases"""
	if len(alist)<=2:
		return aterm in alist
	if alist[len(alist)//3]==aterm:
		return True
	if alist[(len(alist)*2)//3]==aterm:
		return True

	"""slices the length of the list depending whether the item we are searching
	for is smller than the 1/3 term in between the 1/3 term and 2/3 term or bigger than
	the 2/3 of the way through term"""
	if aterm<alist[len(alist)//3]:
		return terSearch(alist[:len(alist)//3], aterm)
	elif (aterm>alist[len(alist)//3] and aterm<alist[(len(alist)*2)//3]):
		return terSearch((alist[len(alist)//3:(len(alist)*2)//3]),aterm)
	else:
		return terSearch(alist[(len(alist)*2)//3:],aterm)



def terSearch2(alist, aterm, left, right):

	"""Base cases"""
	if right-left<=2:
		return aterm in alist[left:right]
	if alist[(right-left)//3+left]==aterm:
		return True
	if alist[((right-left)*2)//3+left]==aterm:
		return True

	"""Searchers through list and changes the part of the list it searching through 
	depending on whether the term we are looking for is than the 1/3 term,
	in between the 1/3 term and 2/3 term, or bigger than 
	the 2/3 of the way through term"""
	if aterm<alist[(right-left)//3+left]:
		return terSearch2(alist, aterm, left ,(right-left)//3+left)
	elif (aterm>alist[(right-left)//3+left] and aterm<alist[((right-left)*2)//3+left]):

		return terSearch2(alist, aterm, (right-left)//3+left, ((right-left)*2)//3+left)
	else:
		return terSearch2(alist, aterm, ((right-left)*2)//3+left , right)



def main():
	L = [x*3 for x in range(int(sys.argv[1]))]

	timeBefore=time.time()
	isFound = terSearch2(L, int(sys.argv[2]), 0 , len(L)-1)
	timeAfter=time.time()

	timeBefore2=time.time()
	isFound2= terSearch(L, int(sys.argv[2]))
	timeAfter2=time.time()
	print(isFound)
	print(timeAfter-timeBefore)

	print(isFound2)
	print(timeAfter2-timeBefore2)
main()


