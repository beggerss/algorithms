#!/usr/bin/python2
# Author: Ben Eggers

import time
import numpy as np
import matplotlib.pyplot as plt

# Implementation of mergesort written in Python.

def main():
	base = 1000
	x_points = []
	y_points = []
	for x in range(1, 20):
		arr = [np.random.randint(0, base*x) for k in range(base*x)]
		start = int(round(time.time() * 1000))
		arr = merge_sort(arr)
		end = int(round(time.time() * 1000))
		x_points.append(len(arr))
		y_points.append(end - start)
		print("%d ms required to sort array of length %d using mergesort." 
			% (end - start, len(arr)))
	make_plot(x_points, y_points)

def merge_sort(arr):
	length = len(arr)
	if length <= 1:
		return arr
	# cut the array in 2
	first = arr[:length/2]
	last = arr[length/2:]
	# sort both halves
	first = merge_sort(first)
	last = merge_sort(last)
	# now put them together
	results = []
	while len(first) > 0 or len(last) > 0:
		if len(first) is 0:
			results.append(last[0])
			del last[0]
		elif len(last) is 0:
			results.append(first[0])
			del first[0]
		elif first[0] < last[0]:
			results.append(first[0])
			del first[0]
		else:
			results.append(last[0])
			del last[0]
	return results

def make_plot(x_points, y_points):
	plt.plot(x_points, y_points, 'ro')
	plt.axis([0, max(x_points), 0, max(y_points)])
	plt.xlabel('length of array')
	plt.ylabel('time to sort (milliseconds)')
	plt.title('Efficiency of merge sort')
	plt.show()

if __name__ == "__main__":
	main()