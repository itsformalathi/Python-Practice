# project Euler - Problem 3: Largest prime factor

""" The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

def primeFactors(number):
    """ return the list of prime factors for a given number"""
    factorlist=[]
    loop=2
    while loop<=number:
          if number%loop==0:
             number/=loop
             factorlist.append(loop)
          else: 
              loop+=1
    return factorlist

def largestPrimeFactor(number):
    """ returns the maximum prime factor from the given list"""
    factorlist = primeFactors(number)
    maximumfactor = max(factorlist)
    return maximumfactor

def main():
    number = int(input("enter the number : "))
    largestfactor = largestPrimeFactor(number)
    print(largestfactor)

main()

