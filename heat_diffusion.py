#!/usr/bin/python2
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
	print(bounds)
	name = raw_input("What should the generated image be called?: ")
	if name is "":
		raise "Come on, pick a name"
	# Now, generate the grid
	grid = np.array([np.array([0 for y in range(gridy)]) for x in range(gridx)])
	
	print("Do you want to:\n\
	1)	Use Monte Carlo to generate the image\n\
	2)	Use Jakobi iteration to generate the image\n\
	3)	Use Jakobi iteration to generate a gif (slow, and requires imagemagik)\n\
	4) 	Do both and compare runtime/number of computations\n")
	answer = input("Answer (default is 1): ")
	if answer is 2:
		grid = jakobi(grid, bounds)
	elif answer is 3:
		jakobi_gif(grid, name)
	elif answer is 4:
		compare(grid, bounds)
	else:
		grid = monte_carlo(grid, bounds)
	generate_map(grid, name)

def monte_carlo(grid, bounds):
	pass

def jakobi(grid, bounds):
	pass

def jakobi_gif(grid, bounds, name):
	pass

def compare(grid, bounds):
	pass

def generate_map(grid, name):
	pass

if __name__ == "__main__":
	main()