#Project Euler - Problem 4: Largest palindrome product

""" A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers. """

def largestPalindrome():
    """ returns n which is the largest palindrome made from two numbers in the range 100 to 999"""
    n = 0
    for a in range(999, 100, -1):
        for b in range(a, 100, -1):
            x = a * b
            if x > n:
               s = str(x)
               if s == s[::-1]:
                  n = a * b
    return n              

def main():
    print(largestPalindrome())

main()    
