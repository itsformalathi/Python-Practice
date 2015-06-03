""" To print the difference of Sum of squares of first 100 natural numbers      and square of their sum"""

Start = 1
Limit = 100

def Square(i):
    return (i * i)

def Sum2(Start, Limit):
    sum = 0
    for i in range(Start, Limit+1):
        sum += i
    return Square(sum)    

def Sum1(Start, Limit):
    sum = 0
    for i in range(Start, Limit+1):
        sum += Square(i)
    return sum

def main():
    diff = (Sum1(Start, Limit) - Sum2(Start, Limit))
    print (diff)

main()
