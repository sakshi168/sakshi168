
#1st Method
def reverse(s):
    str = ""
    for i in s:
	    str = i + str
    return str
print("1st method")
s = input("Enter a string: ")

print ("The original string is : ",end="")
print (s)

print ("The reversed string is : ",end="")
print (reverse(s))


#2nd Method

# Python code to reverse a string using recursion

def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]
print("2nd Method")
s = input("Enter a string: ")

print ("The original string is : ",end="")
print (s)

print ("The reversed string is : ",end="")
print (reverse(s))

#3rd Method

# Python code to reverse a string using reversed()

def reverse(string):
	string = "".join(reversed(string))
	return string

print("3rd method")
s = input("Enter a string: ")

print ("The original string is : ",end="")
print (s)

print ("The reversed string(using reversed) is : ",end="")
print (reverse(s))


