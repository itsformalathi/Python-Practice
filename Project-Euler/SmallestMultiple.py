#Project Euler - Problem 5 : Smallest Multiple

"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
         
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? """

def gcd(a,b): 
    """ returns gcd of a, b """
    return b and gcd(b, a % b ) or a

def lcm(a, b):
    """ returns lcm of a, b """
    return ((a * b) // gcd(a,b))

def lcmof1to20():
    """ calculates the lcm of 1 to 20 """
    n = 1
    for i in range(2, 21):
        n = lcm(n, i)
    return n

def main():
    print(lcmof1to20())

main()
