
Limit = int(input("Enter your limit: "))
num = 1
while num <= Limit:
   for i in range(2,Limit+1):
      if (num % i) == 0:
         break
      else:
         print(num)
   num += 1      
