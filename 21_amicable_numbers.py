# Program to evaluate the sum of all the amicable numbers under 10,000


amicable_numbers = []


# Function getDivisors(num) finds the divisors of any inputted number and runs the getPossiblePair(divisors, checkNum) function on them
def getDivisors(num):
    firstNum = num
    set_of_divisors = []
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            set_of_divisors.append(i)
    getPossiblePair(set_of_divisors, firstNum)


# Function getPossiblePair(divisors, checkNum) checks if the sum of the inputted divisors has an amicable pair
# If the program finds an amicable pair for the sum it adds both the sum and the found pair to the amicable_numbers list

def getPossiblePair(divisors, checkNum):
    possiblePair = 0
    second_set_divisors = []
    possiblePair = sum(divisors)
    for i in range(1, (possiblePair // 2) + 1):
        if possiblePair % i == 0:
            second_set_divisors.append(i)
    if sum(second_set_divisors) == checkNum:
        # The following if statement checks if the found pair is less than 10,000 and only then adds the pair to the amicable_numbers list
        if possiblePair < 10000:
            if possiblePair != checkNum:
                amicable_numbers.append(possiblePair)
                amicable_numbers.append(checkNum)


# Running the getDivisors(num) function on every number from 1 to 10,000
for i in range(1, 10000):
    getDivisors(i)


# Adding all the values of amicable_numbers to list_of_amicables without duplicates
list_of_amicables = []
for i in amicable_numbers:
    if i not in list_of_amicables:
        list_of_amicables.append(i)


# Printing the sum of all the amicable numbers found
print(sum(list_of_amicables))