# Program to print the 10001st prime number

# Funcion isPrime(num) checks if number is prime or not
def isPrime(num):
    import math
    i = 2
    for i in range(2, (int)(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

# Function getPrimes adds all prime numbers to the Primes list
def getPrimes(num):
    i = 2
    Primes = []
    while True:
        if isPrime(i):
            Primes.append(i)
        i += 1
        if len(Primes) == num:
            break
    return Primes[num - 1]

# Printing the 10001st prime number from the list of Primes
print(getPrimes(10001))