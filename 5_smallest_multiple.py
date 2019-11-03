# Program to find the smallest positive number that is evenly divisible by all numbers 1 to 20

# Function isDivisible(num) checks whether inputted number meets the condition
def isDivisible(num):
    for x in range(2,21):
        if num % x != 0:
            return False
    return True

# Trying all possibilites of num until the condition is satisfied starting with 20 and if not
# increment by 20
num = 20
while True:
    if isDivisible(num):
        break
    num += 20


# Finally printing out the smallest number that is evenly divisible by all numbers 1 to 20
print(num)
