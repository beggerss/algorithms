#!/usr/bin/python
# Author: Ben Eggers

# Finds the GCD of two integers gotten from the user using Euclid's algorithm
# (Euclid was a pretty smart dude)
# Here's how it works:

# If either of the passed numbers is 0, return whatever the other number is (duh).
# If passed a and b s.t. a > b and a != 0 and b != 0, recursively call the
# GCD function, but this time with a % b and b. Eventually one of them will
# reach 0, and the other one will be the GCD.

def main():
	a = input("Please enter a value for a: ")
	b = input("Please enter a value for b: ")
	gcd = GCD(a, b)
	print("GCD(%d, %d) = %d" % (a, b, gcd))


def GCD(a, b):
	if a is 0:
		return b
	elif b is 0:
		return a
	if a > b:
		return GCD(a % b, b)
	else:
		return GCD(a, b % a)

if __name__ == "__main__":
	main()