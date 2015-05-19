from random import randint
number = randint(0, 10)
print (number)
#Guess = int(input("Guess your number between 0 and 10: "))
for turn in range(3):
    Guess = int(input("Guess your number between 0 and 10: "))
    if Guess == number:
       print("Congratulations! you got it")
       break
    else:
       if Guess < 0 or Guess > 10:
          print("oops! you are not even in range.Enter bet 0 and 10: ")
       elif Guess < number:
          print("you are low")
       else:
          print("you are high")    
print("Game Over")
