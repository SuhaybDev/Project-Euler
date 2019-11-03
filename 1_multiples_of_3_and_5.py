# Program for finding sum of multiples of 3 and 5 below 1000
def computeSum():
	ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
	return str(ans)


if __name__ == "__main__":
	print(computeSum())