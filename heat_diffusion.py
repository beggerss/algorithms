#!/usr/bin/python
# Author: Ben Eggers

import math # for math
import numpy as np # for faster math
import PIL # for pretty math
import random # for random math

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
 into?: ")
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
  3)  Do both and compare the number of computations\n\
  4)  Use Jakobi iteration to generate a gif (slow, and requires imagemagick)")
	answer = raw_input("Answer: ")
	if answer is "3":
		compare(grid)
	else: # necessary because compare doesn't return a grid or # of computations
		if answer is "1":
			grid, computations = monte_carlo(grid)
		elif answer is "2" or answer is "4":
			grid, computations = jakobi(grid, (answer is "4"))
		else:
			print("Invalid answer. Quitting...")
		print("%d computations done." % computations)
		generate_map(grid, name)

def monte_carlo(grid):
	"""
	Finds a close approximation to the stable heat distribution on the grid
	using n random walks on each point. Parameters are:
	1) The grid. Boundaries should already be set.
	Returns:
	A (grid, computations)-tuple.
	"""	
	iterations = input("How many random walks should be done on each point? ")
	computations = 0
	for x in range(1, len(grid) - 1): # don't want the boundaries
		for y in range(1, len(grid[x]) - 1):
			# Now we're iterating over each point to do a random walk for
			total = 0
			for iteration in range(iterations):
				# random walk 'iterations' times
				current_pos = np.array([x, y])
				# while we're not at an edge
				while current_pos[0] > 0 and current_pos[0] < len(grid) - 1 and\
						current_pos[1] > 0 and current_pos[1] < len(grid[x]) - 1:
					direction = np.random.randint(0, 3)
					computations += 2 # one for the random number, one for the increment
					if direction is 0:
						current_pos[0] += 1 # right
					elif direction is 1:
						current_pos[1] += 1 # down
					elif direction is 2:
						current_pos[0] -= 1 # left
					else:
						current_pos[1] -= 1 # up
				# now add the boundary to total so we can average them later
				total += grid[current_pos[0]][current_pos[1]]
				computations += 1
			# Now we've done some number of random walks and have the total of
			# the boundaries we hit, so average them and record it.
			grid[x][y] = 1.0 * total / (iterations * 1.0)
			computations += 2
			print("Point (%d, %d) complete!" % (x, y))
	return (grid, computations)

def jakobi(grid, gif=False):
	"""
	Finds a  the stable heat distribution on the grid using Jakobi iteration.
	Parameters are:
	1) The grid. Boundaries should already be set.
	Returns:
	A (grid, computations)-tuple.
	"""
	computations = 0
	keep_going = True
	while keep_going:
		keep_going = False # will be set to True on changing a value
		for x in range(1, len(grid) - 1):
			for y in range(1, len(grid[x]) - 1):
				new = (grid[x-1][y] + grid[x+1][y] + grid[x][y-1] + grid[x][y+1]) / 4
				computations += 8
				if new != grid[x][y]:
					keep_going = True
					grid[x][y] = new
	return (grid, computations)

def jakobi_single_iteration(grid):
	"""
	Does a single Jakobi averaging iteration on the passed grid.
	Parameters are:
	1) The grid.
	Returns:
	A (grid, computations)-tuple.
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