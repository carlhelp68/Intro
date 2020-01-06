import sys
def search_linear(x,y):
  n = len( x )
  for i in range(n):
  	if x[i] == y:
  		return True
  return False
def main():
	L = [x*3 for x in range(100)] 
	isFound = search_linear(L, int(sys.argv[1])) 
	print(isFound)
main()
