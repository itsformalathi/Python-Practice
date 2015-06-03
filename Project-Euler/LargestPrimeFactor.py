# The largest prime factor of 600851475143

def primefactors(number):
    factorlist=[]
    loop=2
    while loop<=number:
          if number%loop==0:
             number/=loop
             factorlist.append(loop)
          else: 
              loop+=1
    return factorlist

def LargestPrimeFactor(number):
    factorlist = primefactors(number)
    maximumfactor = max(factorlist)
    return maximumfactor

def main():
    number = int(input("enter the number : "))
    largestfactor = LargestPrimeFactor(number)
    print(largestfactor)

main()
