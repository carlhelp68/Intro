def mystery(s):
	if len(s)==0:
		return False
	elif len(s) ==1:
		return True
	else:
		print(s[1:-1])
		return mystery(s[0:-2])
def main():
	s = [1,2,3,4,5,6,7,9]
	ttt=mystery(s)
	print(ttt)
main()