import math

factors = []
prime_factors =[]

def getFactors(num):
    for possibleFactor in range(1, int(math.sqrt(num)) + 1):
        if num % possibleFactor == 0:
            factors.append(possibleFactor)
            factors.append(num / possibleFactor)

getFactors(24)

def isPrime():
    for anyNum in factors:
        for i in range(int(anyNum)):
            if (anyNum % i) == 0:
                prime_factors.append(anyNum)
    print(prime_factors)


isPrime()
