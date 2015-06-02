""" To print the difference of Sum of squares of first 100 natural numbers      and square of their sum"""

Start = 1
Limit = 100
sum1 = 0
sum2 = 0

def Square(i):
    return (i * i)
def Sum2(sum1):
    for i in range(Start, Limit+1):
        sum1 += i
    return Square(sum1)    
def Sum1(sum2):
    for i in range(Start, Limit+1):
        sum2 += Square(i)
    return sum2
diff = (Sum1(sum1) - Sum2(sum1))
print (diff)
