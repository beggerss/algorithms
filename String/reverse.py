# Author: Ben Eggers

# Reverses a string

def main():
	print reverse("Hey, Python is fun!")

def reverse(str):
	result = ""
	for x in str:
		result = x + result
	return result

if __name__ == "__main__":
	main()