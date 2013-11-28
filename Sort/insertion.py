#!/usr/bin/python2
# Author: Ben Eggers

import time
import numpy as np
import matplotlib.pyplot as plt\

# Implementation of intsertion sort in Python.

def main():
	base = 1000
	x_points = []
	y_points = []
	for x in range(1, 20):
		arr = [np.random.randint(0, base*x) for k in range(base*x)]
		start = int(round(time.time() * 1000))
		arr = insertion_sort(arr)
		end = int(round(time.time() * 1000))
		x_points.append(len(arr))
		y_points.append(end - start)
		print("%d ms required to sort array of length %d using insertion sort." 
			% (end - start, len(arr)))
	make_plot(x_points, y_points)

def insertion_sort(arr):
	

def make_plot(x_points, y_points):
	plt.plot(x_points, y_points, 'ro')
	plt.axis([0, max(x_points), 0, max(y_points)])
	plt.xlabel('length of array')
	plt.ylabel('time to sort (milliseconds)')
	plt.title('Efficiency of insertion sort')
	plt.show()

if __name__ == "__main__":
	main()