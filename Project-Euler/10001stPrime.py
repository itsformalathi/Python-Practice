#Project Euler - Problem 7: 10001st prime

""" By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number? """

def isPrime(n):
    """ checks whether a number is prime """
    for i in range(3, n//2, 2):
        if n % i == 0: 
           return False
    return True    

def generate10001stPrimenumber():
    """ returns 10001st prime """
    num = 1
    count = 1
    while count < 10001:
          num += 2
          if isPrime(num):
             count += 1
    return num

def main():
    print (generate10001stPrimenumber())

main()
