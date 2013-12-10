# Author: Ben Eggers
# Reverses an array in-place

def main():
	print reverse([1,2,3,4,5,6])

def reverse(arr):
	for x in range(len(arr) / 2):
		tmp = arr[x]
		arr[x] = arr[len(arr) - x - 1]
		arr[len(arr) - x - 1] = tmp
	return arr


if __name__ == "__main__":
	main()