counter = 0
L = [1,2,3, 4]
L=L[1:-1:]
print(L)

for i in range(len(L)):
	counter +=1
if counter%2==0:
	print("Even")
else:
	print("odd")