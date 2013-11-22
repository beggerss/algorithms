#!/usr/bin/python
# Author: Ben Eggers

import math # for math
import numpy as np # for faster math
import PIL # for pretty math

# This script can be used several ways: the first is to calculate the final
# heat distribution in a metal plate given user input for parameters using
# either Jakobi iteration or a Monte Carlo method. The second is to do both,
# and compare the relative speed and accuracy of the two. The third is to
# use Jakobi iteration but take a snapshot every n iterations then stitch them
# into a gif.

def main():
	gridx = input("X length of grid (px)?: ")
	gridy = input("Y length of grid (px)?: ")
	area_count = input("How many areas would you like each edge to be divided\
 into (1 - min(x, y))?: ")
	bounds = [[],[],[],[]] # one array for each edge
	for x in range(area_count):
		bounds[0].append(input("Temperature in area %d of top? " % (x+1)))
	for x in range(area_count):
		bounds[1].append(input("Temperature in area %d of right? " % (x+1)))
	for x in range(area_count):
		bounds[2].append(input("Temperature in area %d of left? " % (x+1)))
	for x in range(area_count):
		bounds[3].append(input("Temperature in area %d of bottom? " % (x+1)))
	name = raw_input("What should the generated image be called?: ")
	while name is "":
		name = raw_input("Come on, pick a name: ")
	# Now, generate the grid
	# The for loops go through area 1 of the top, right, bottom, middle, then area
	# 2, etc. Each time it loops through an area and a side, it sets all the 
	# grid values of that area of the side to the value found in the bounds array.
	grid = np.array([np.array([0 for y in range(gridy)]) for x in range(gridx)])
	for area in range(area_count):
		# Top
		for x in range((gridx * area / area_count), (gridx * (area + 1) / area_count)):
			grid[x][0] = bounds[0][area]
		# Right
		for y in range((gridy * area / area_count), (gridy * (area + 1) / area_count)):
			grid[gridx - 1][y] = bounds[1][area]
		# Bottom
		for x in range((gridx * area/ area_count), (gridx * (area + 1) / area_count)):
			grid[x][gridy - 1] = bounds[2][area]
		# Left
		for y in range((gridy * area / area_count), (gridy * (area + 1) / area_count)):
			grid[0][y] = bounds[3][area]
	print("Do you want to:\n\
  1)  Use Monte Carlo to generate the image\n\
  2)  Use Jakobi iteration to generate the image\n\
  3)  Do both and compare runtime/number of computations\n\
  4)  Use Jakobi iteration to generate a gif (slow, and requires imagemagick)")
	answer = raw_input("Answer (default is 1): ")
	if answer is "2":
		grid = jakobi(grid)
	elif answer is "3":
		compare(grid)
	elif answer is "4":
		jakobi_gif(grid)
	else:
		grid = monte_carlo(grid)
	generate_map(grid, name)

def monte_carlo(grid, cmp=False):
	"""
	Finds a close approximation to the stable heat distribution on the grid
	using n random walks on each point. Parameters are:
	1) The grid. Boundaries should already be set.
	Returns:
	A (grid, (time, computations)-tuple)-tuple.
	"""	
	iterations = input("How many random walks should be done on each point? ")


def jakobi(grid, cmp=False):
	"""
	Finds a  the stable heat distribution on the grid using Jakobi iteration.
	Parameters are:
	1) The grid. Boundaries should already be set.
	Returns:
	A (grid, (time, computations)-tuple)-tuple.
	"""
	pass

def jakobi_gif(grid, delete=True):
	"""
	Generates a gif of heat diffusing through the grid (imagemagick required).
	Parameters are:
	1) The grid. Boundaries should already be set.
	2) A boolean telling whether or not to delete the individual frames after
		creating the gif (True by default).
	Returns:
	A (grid, (time, computations)-tuple)-tuple.
	"""
	pass

def jakobi_single_iteration(grid):
	"""
	Does a single Jakobi averaging iteration on the passed grid.
	Parameters are:
	1) The grid.
	Returns:
	Nothing.
	"""
	pass

def compare(grid):
	"""
	Finds the final heat distribution using jakobi iteration and Monte Carlo,
	then prints out some statistics about relative runtime/number of computations.
	Parameters are:
	1) The grid. Boundaries should already be set.
	Returns:
	Nothing.
	"""
	pass

def generate_map(grid, name):
	"""
	Generates a heatmap image of the passed grid.
	Parameters are:
	1) The grid. Heat distribution should already have been found.
	2) The name of the file to write the heatmap out to.
	Returns:
	Nothing.
	"""
	pass

if __name__ == "__main__":
	main()