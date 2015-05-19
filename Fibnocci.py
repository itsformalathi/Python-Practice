def fib(number):
    a, b = 0, 1
    print (a)
    sum = 1
    while sum < number:
          print (sum)
          sum += a
          a, b = b, a+b
    print()      
fib(int(input("Enter a limit: ")))
