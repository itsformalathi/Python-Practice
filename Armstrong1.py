def num2digits(number):
    digits = list(str(number))
    return digits

def powerofdigits(number, numDigits):
    return int(number) ** numDigits

def sumofpowers(number):
    sum = 0
    digits = num2digits(number)
    for i in range(len(digits)):
        sum += powerofdigits(digits[i], len(digits))
    return sum

def IsArmstrong(number):
    if number == sumofpowers(number):
       return True
    return False

start = 100
limit = 10000
for number in range(start, limit):
    if IsArmstrong(number):
        print(number)
