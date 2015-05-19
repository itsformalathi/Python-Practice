def collatz(n):
   while n > 1:
       if n % 2 == 0:
          n = n // 2
          print (n, end = " ")
       else:
          n = (3 * n) +1
          print (n, end = " ")
   print()
start = 10
limit = 20
for i in range(start, limit):
    collatz(i)
