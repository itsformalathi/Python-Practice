def ExtractDigits(number):
   """units = number % 10
    number = number // 10
    tens = number % 10
    number = number // 10
    hundreds = number % 10
    return units, tens, hundreds """
   digits = []
   while number > 0:
        remainder = number % 10
        digits.append(remainder)
        number = number // 10
   return digits

def isnotEvendigit(digits):   
  for num in digits:
      if num % 2 != 0:
         print (num)
         return num
number = int(input("input a three digit number: "))
digits = ExtractDigits(number)
if isnotEvendigit(digits):
   print ("%d does not have all even Numbers"%(number))
else: 
  print ("%d has all even Numbers"%(number))

