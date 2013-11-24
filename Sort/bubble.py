#!/usr/bin/python
# Author: Ben Eggers

import numpy as np
import time

# Implementation of a bubble sort in Python.

def main():
	base = 10
	for x in range(1, 5):
		arr = [np.random.randint(0, base**x) for k in range(base**x)]
		start = int(round(time.time() * 1000))
		bubble_sort(arr)
		end	= int(round(time.time() * 1000))
		print("%d ms required to sort array of length %d."% (end - start, len(arr)))

def bubble_sort(arr):
	keep_going = True
	length = len(arr)
	while keep_going:
		keep_going = False # will be True if elements are switched
		for x in range(length - 1):
			if arr[x] > arr[x + 1]:
				tmp = arr[x]
				arr[x] = arr[x + 1]
				arr[x + 1] = tmp
				keep_going = True
	return arr

if __name__ == "__main__":
	main()