def FibnocciList(limit):
    a, b = 0, 1
    sum = 1
    fiblist = [a]
    while sum <= limit:
          fiblist.append(sum)
          sum += a
          a, b = b, a+b
    return fiblist

def SumofEvenfibnocci(fiblist):
    sumeven = 0
    for i in fiblist:
        if i % 2 == 0:
           sumeven += i
    return sumeven       

def main():
    limit = int(input("Enter a limit: "))
    fiblist = FibnocciList(limit)
    print (fiblist)
    sumeven = SumofEvenfibnocci(fiblist)
    print(sumeven)

main()    
