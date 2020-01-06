##letter to n'th letter of alphabet
#letter = input("Please enter a letter: ")

#value=ord(letter)
#value = value - 96
#print(value)

#different but less efficient way of doing
#alphabet="abcdefghijklmnopqrstuvwxyz"
#print(alphabet[n-1])



#number to letter using ASCII

value = input("Please enter a number: ")
value = int(value)
letter=chr(value+96)
print(letter)