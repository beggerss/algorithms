#!/usr/bin/python2
# Author: Ben Eggers (ben@beneggers.com)

import numpy as np
import time
import matplotlib.pyplot as plt

# Implementation of a bubble sort in Python.

def main():
	base = 200
	x_points = []
	y_points = []
	for x in range(1, 20):
		arr = [np.random.randint(0, base*x) for k in range(base*x)]
		start = int(round(time.time() * 1000))
		bubble_sort(arr)
		end = int(round(time.time() * 1000))
		x_points.append(len(arr))
		y_points.append(end - start)
		print("%d ms required to sort array of length %d using bubble sort."
			% (end - start, len(arr)))
	make_plot(x_points, y_points)

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

def make_plot(x_points, y_points):
	plt.plot(x_points, y_points, 'ro')
	plt.axis([0, max(x_points), 0, max(y_points)])
	plt.xlabel('length of array')
	plt.ylabel('time to sort (milliseconds)')
	plt.title('Efficiency of bubble sort')
	plt.show()

if __name__ == "__main__":
	main()