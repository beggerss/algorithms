#!/usr/bin/python2
# Author: Ben Eggers

import math # for math
import numpy # for faster math
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
	area_count = input("How many areas would you like each edge to be divided \
		into (1 - min(x, y))?: ")
	bounds = [[],[],[],[]] # one array for each edge
	for x in range(area_count):
		bounds[0].append(input("Temperature in area %d of top? ") % (x+1))
	for x in range(area_count):
		bounds[0].append(input("Temperature in area %d of right? ") % (x+1))
	for x in range(area_count):
		bounds[0].append(input("Temperature in area %d of left? ") % (x+1))
	for x in range(area_count):
		bounds[0].append(input("Temperature in area %d of bottom? ") % (x+1))
	grid = None
	

	generate_map(grid)

def jakobi(...):


def monte_carlo(...):


def generate_map(grid):
	raise "Something went wrong" if grid is None


if __name__ == "__main__":
	main()