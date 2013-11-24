#!/usr/bin/python2
# Author: Ben Eggers (ben@beneggers.com)

import time
import numpy as np
import matplotlib.pyplot as plt
import itertools

# Implementation of a quicksort in Python.

def main():
	base = 10000
	x_points = []
	y_points = []
	for x in range(1, 20):
		arr = [np.random.randint(0, base*x) for k in range(base*x)]
		start = int(round(time.time() * 1000))
		arr = quick_sort(arr)
		end = int(round(time.time() * 1000))
		x_points.append(len(arr))
		y_points.append(end - start)
		print("%d ms required to sort array of length %d using quicksort." 
			% (end - start, len(arr)))
	make_plot(x_points, y_points)

def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	# There are many ways to choose a pivot, we'll just grab a random element
	pivot_index = np.random.randint(0, len(arr) - 1)
	pivot = arr[pivot_index]
	del arr[pivot_index]
	less = []
	greater = []
	for x in arr:
		if x <= pivot:
			less.append(x)
		else:
			greater.append(x)
	lists = [quick_sort(less), [pivot], quick_sort(greater)]
	# pivot must be in its own sublist for the below list comprehension to work
	return [item for sublist in lists for item in sublist]

def make_plot(x_points, y_points):
	plt.plot(x_points, y_points, 'ro')
	plt.axis([0, max(x_points), 0, max(y_points)])
	plt.xlabel('length of array')
	plt.ylabel('time to sort (milliseconds)')
	plt.title('Efficiency of quick sort')
	plt.show()

if __name__ == "__main__":
	main()