#!/usr/bin/python2
# Author: Ben Eggers


def main():
	for base in [10, 100, 200]:
		x_points = []
		y_points = []
		for x in range(1, 25):
			arr = [np.random.randint(0, base*x) for k in range(base*x)]
			start = int(round(time.time() * 1000))
			arr = selection_sort(arr)
			end = int(round(time.time() * 1000))
			x_points.append(len(arr))
			y_points.append(end - start)
			print("%d ms required to sort array of length %d using selection sort." 
				% (end - start, len(arr)))
		make_plot(x_points, y_points)