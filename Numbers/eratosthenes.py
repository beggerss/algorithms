#!/usr/bin/python
# Author: Ben Eggers

import math

# Finds prime numbers up to a user-generated value using the Sieve of Eratosthenes
# algorithm. The algorithm starts with an index i = 2. Then, it iteratively adds
# the current index number to the primes set, marks all multiples of it (in a boolean
# array) as non-prime, and increments the index to the next unmarked number. Once
# it reaches sqrt(size), it has marked all non-primes and just iterates through
# the boolean array to find the remaining primes.

def main():
	n = input("Enter a number: ")
	print(get_primes(n))

def get_primes(n):
	"""Efficiently get primes up to n (returned in list form)."""
	primes = []
	is_prime = [True for x in range(n)]
	for x in range(2, int(math.ceil(n**.5))):
		if is_prime[x]:
			y = 2 * x
			while y <= n - 1:
				is_prime[y] = False
				y += x
	for x in range (2, n):
		if is_prime[x]:
			primes.append(x)
	return primes

if __name__ == "__main__":
	main()