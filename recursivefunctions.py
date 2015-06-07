# Recurrsive Functions

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def iterative_factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result   

#The Fibonacci numbers are easy to write as a Python function. It's more or less a one to one mapping from the mathematical definition:
# A recurrsive function for Fibnocci numbers

def fib(n):
    if n == 0:
       return 0
    elif n == 1:
       return 1
    else:
       return fib(n-1) + fib(n-2)

#Think of a recusive version of the function f(n) = 3 * n, i.e. the multiples of 3

def mult3(n):
    if n == 1:
       return 3
    else:
       return mult3(n-1) + 3

for i in range(1,10):
    print(mult3(i))

#Write a recursive Python function that returns the sum of the first n integers.

def Sum_n(n):
    if n==0:
       return 0
    else:
       return n + sum_n(n-1)

