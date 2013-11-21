#!/usr/bin/python
# Author: Ben Eggers

# Finds the maximum element in a user-defined array.
# This could be done by just checking each value as the user puts them in,
# but the purpose is to illustrate how to do it if passed an arbitrary array.

def main():
	size = input("How many elements would you like to put in the array? ")
	arr = []
	for x in range(size):
		arr.append(input("Element %d: " % (x+1)))
	amax, index = find_max(arr)
	print("Max element is %d at index %d." % (amax, index))

def find_max(arr):
	amax = None
	index = -1
	for x in range(len(arr)):
		if arr[x] > amax:
			amax = arr[x]
			index = x
	return amax, index

if __name__ == "__main__":
	main()