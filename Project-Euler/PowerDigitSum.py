# ProjectEuler - problem 16 - Power digit sum
""" 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000? """

import math
number = pow(2, 1000)
result = str(number)
sum = 0
for i in result:
    sum += int(i)
print(sum)
