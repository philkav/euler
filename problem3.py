#!/usr/bin/python
from sys import exit, argv

def isPrime(number):
	i = 2
	while i < number:
		if number % i == 0:
			return False
		i+=1
	return True
def getPrimeNumbers(factor):
	i = 2
	while i < factor:
		if isPrime(i): yield i
		i+=1

if len(argv) < 2:  exit("Use properly")

factor = int(argv[1])

for i in getPrimeNumbers(factor):
	 if factor % i == 0: print i
