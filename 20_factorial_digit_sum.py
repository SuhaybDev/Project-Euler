# Program to find the sum of the digits in the factorial of 100


# Funcion getFactorial(num) is a recursive function that outputs the factorial of any inputted number
def getFactorial(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    else: 
        return num * getFactorial(num - 1)


# Fuction digitSum() finds the sum of the digits in the factorial of 100
def digitSum():
    factorial = getFactorial(100)
    digits = list(str(factorial))
    sum = 0
    for digit in digits:
        sum += int(digit)
    print(sum)


# Calling the digitSum() function to get the answer
digitSum()