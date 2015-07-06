# Project Euler - Problem 15 - Lattice paths
""" Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner
How many such routes are there through a 20×20 grid?"""

def factorial(n):
    """ n! = n*(n-1)*(n-2)....1 """
    factorialValue = 1
    while n > 1:
        factorialValue *= n
        n -= 1
    return factorialValue

def numberCombinations(n, k):
    """ The formula used to find how many ways we can choose k elements from n is n!/ k! * (n-k)! """
    numberOfcombinations = factorial(n) / (factorial(k) * factorial(n - k))
    return numberOfcombinations

def main():
    """ Determining the number of routes for a square grid (n × n) is the     central binomial coefficient or the center number in the 2nth row of Pascal's triangle. """
    result = numberCombinations(40,20)
    print(result)

main()
