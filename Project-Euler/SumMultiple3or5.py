# Project Euler - Problem 1: Multiples of 3 and 5
""" If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000 """

def sumMultiple3or5(limit):
    """ returns sum of all multiples of 3 or 5 for a given limit """
    a = 0
    sum = 0
    while a < limit:
        if a%3 == 0 or a%5 == 0:
            sum += a
        a = a+1    
    return sum

def main():
    print(sumMultiple3or5(int(input("Enter the limit :"))))

main() 
