# Program to find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum

# Finding sum of the squares
sumSquare = 0
for i in range(1,101):
    sumSquare += i * i

# Finding the square of the sum
squareSum = 0
for i in range(1,101):
    squareSum += i
squareSum = squareSum * squareSum

# Printing the difference
print(squareSum - sumSquare)