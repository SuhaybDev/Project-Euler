# Program for finding the sum of those even valued terms in fibonacci sequence whose values
# do not exceed 4000000
def compute():
	ans = 0
    # First fibonacci number
	x = 1 
    # Second fibonacci number 
	y = 2  
	while x <= 4000000:
		if x % 2 == 0:
			ans += x
		x, y = y, x + y
	return str(ans)


if __name__ == "__main__":
	print(compute())