number = 1
limit = int(input("Enter a limit: "))
i = 1
while i < limit or condition == "quit":
    for j in range(i):
        if number == limit:
           condition = "quit"
           break
        else:
           print(number, end = " ")
        number += 1   
        print()
