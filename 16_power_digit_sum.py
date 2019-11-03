# Program to find the sum of the digits of the number 2^1000


# Finding 2 to the 1000th power
num = 2**1000


# The function digitSum(num) finds the sum of its digits
def digitSum(num):
    num_str = str(num)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    return sum


# Printing the sum
print(digitSum(num))

