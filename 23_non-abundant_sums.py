'''
Program to find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
(A number n is called abundant if the sum of its proper divisors exceeds n)
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers
'''


def getSum():
    # Creating a dictionary for number from 1 to 28123
    nums = {}

    # Creating a list to contain all abundant numbers found
    abundant_numbers = []

    # Adding numbers from 1 to 28123 to nums dictionary with the key and value being the number itself
    for i in range(1, 28124):
        nums[i] = i

    # Checking for abundant numbers in nums adding any abundant numbers found to the abundant_numbers list 
    for i in nums:
        if i < sum(factorise(i)):
            abundant_numbers.append(i)

    # Removing numbers from the nums dict if they are the sum of any two numbers from the abundant_numbers list
    for num1 in abundant_numbers:
        for num2 in abundant_numbers:
            total = num1 + num2
            if total in nums:
                nums.pop(total)
    # Printing the sum of all the numbers left in the nums dict
    print(sum(nums))


# Function factorise(num) finds the divisors of any inputted number
def factorise(num):
    factors = []
    x = 1
    while x < num:
        if num % x == 0:
            factors.append(x)
        x += 1
    return(factors)


# Calling the getSum() function to get the solution
getSum()


  



