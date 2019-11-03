# Program to find the largest palindrome made from two 3-digit numbers
def getPalNum():
	largestPalindrome = max(i * j
		for i in range(100, 1000)
		for j in range(100, 1000)
		if str(i * j) == str(i * j)[ : : -1])
	print(int(largestPalindrome))
    

getPalNum()