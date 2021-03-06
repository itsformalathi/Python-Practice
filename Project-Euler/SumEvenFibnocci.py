#Project Euler - Problem 2: Even Fibonacci numbers

""" Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. """

def fibnocciList(limit):
    """ Returns the list of fibnocci numbers up to the given limit """
    a, b = 0, 1
    sum = 1
    fiblist = [a]
    while sum <= limit:
          fiblist.append(sum)
          sum += a
          a, b = b, a+b
    return fiblist

def sumofEvenFibnocci(fiblist):
    """ Returns the sum of even numbers from fibnocci list"""
    sumeven = 0
    for i in fiblist:
        if i % 2 == 0:
           sumeven += i
    return sumeven       

def main():
    limit = int(input("Enter a limit: "))
    fiblist = fibnocciList(limit)
    sumeven = sumofEvenFibnocci(fiblist)
    print(sumeven)

main()
