# Author: Ben Eggers

# Checks if a string is a palindrome or not

def main():
	print palindrome("aoeueoa") # true
	print palindrome("aoeueo") # false

def palindrome(str):
	# use iteration instead of recursion since strings can be looooong
	for x in range(len(str)):
		if str[x] is not str[len(str) - x - 1]:
			return False
		x += 1
	return True

if __name__ == "__main__":
	main()