def isArmstrong(number):
    list = [char for char in str(number)]
    return sum([pow(int(i),len(list))for i in list]) == int("".join(list))
def inputNumber(message):
    try:
        number=int(raw_input(message))
    except ValueError:
        number = "NAN"
    return number
number = inputNumber("input a number:")
while number == "NAN":
    number=inputNumber("you entered noninteger. Please enter intiger")
if isArmstrong(number):
   print "%d is Armstrong Number"%(number)
else:
    print"%d is not Armstrong NUmber"%(number)
