# Project Euler - Problem-10:  "Summation of primes"

"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
   Find the sum of all the primes below two million."""

def isPrime(num):
    """ checks whether a number is prime"""
    for i in range(2, (int(num ** 0.5) + 1)):
        if (num % i) == 0:
            return False
    return True

def sumofPrimes(limit):
    """ returns the sum of primes for a given limit"""
    sum = 0
    for i in range(2, limit+1):
        if isPrime(i):
           sum += i
    return sum

def main():
    limit = int(input("enter a limit"))
    sum = sumofPrimes(limit)
    print (sum)
main()    
