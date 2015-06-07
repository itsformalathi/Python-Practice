#Project Euler - Problem 5: Sum square difference

""" The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. """

Start = 1
Limit = 100

def Square(i):
    """ returns the square of a given number """
    return (i * i)

def Sum2(Start, Limit):
    """ returns the square of sum of numbers ranging from 1 to 100 """
    sum = 0
    for i in range(Start, Limit+1):
        sum += i
    return Square(sum)    

def Sum1(Start, Limit):
    """ returns the sum of squares of 1 to 100 numbers """
    sum = 0
    for i in range(Start, Limit+1):
        sum += Square(i)
    return sum

def main():
    diff = (Sum1(Start, Limit) - Sum2(Start, Limit))
    print (diff)

main()
