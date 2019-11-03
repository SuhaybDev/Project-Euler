'''
Program to find which starting number, under one million, produces the longest collatz chain
Note: This is a brute force solution to the problem
'''
curNum = 0
highest = 0

# Function Collatz(i) generates next collatz number for a given integer
def Collatz(i):
    counter = 1
    while i != 1:
        counter = counter + 1
        if i%2 == 0:
            i = i / 2
        else:
            i = 3*i + 1
    return counter



# Testing for all numbers between 1 to 1000000 and if the number generated has a longer chain 
# than the previous number then store it and continue testing
for i in range(1,1000000):
    curNum = Collatz(i)
    if curNum > highest:
        highest = curNum
        number = i


# Printing out the number with the longest collatz chain
print(number)