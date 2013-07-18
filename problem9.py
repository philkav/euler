#!/usr/bin/python
import math
def calculate_c(a,b):
	c = a*a + b*b
	c = math.sqrt(c)	
	return c

for a in range(0,2220):
	for b in range(0,2220):
		c = calculate_c(a,b)
		if a + b + c == 1000:
			print a * b * c 
