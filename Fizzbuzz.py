import sys

def Multipleof15(i):
    return (i % 15) == 0

def Multipleof3(i):
    if i % 3 == 0:
       return True
    return False

def Multipleof5(i):
    if i % 5 == 0:
       return True
    return False

if len(sys.argv) == 1:
   print ("pass the argument")
   exit()
limit = int(sys.argv[1])   
for i in range(1, (limit + 1)):
    if Multipleof15(i):
       print ("Fizz Buzz")
    elif Multipleof3(i):
       print ("Fizz")
    elif Multipleof5(i):
       print ("Buzz")
    else:
       print (i)
