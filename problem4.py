#!/usr/bin/python


def isPalindrome(string):
	## Return true if a number is a palindrome ##
	if len(string) < 2: return True
	else:
		if string[0] == string [-1]: return isPalindrome(string[1:-1])
		else: return False	

def getPalindromes(max_no):
	## Generator that yields all palindrome products of 2 factors up to max_no##
	current_largest = 0
	for i in range(0,max_no):
		for j in range(0,max_no):
			numStr = str(i*j)	
			if (isPalindrome(numStr)):
				if i*j > current_largest: 
					current_largest = i*j
					yield i,j

## Main ##
max_no = 1000
for i,j in getPalindromes(max_no):
	x,y,z = i,j,i*j 

print x,'*',y,'=',z
