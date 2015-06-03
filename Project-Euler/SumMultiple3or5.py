def SumMultiple3or5(number):
    number = int(number)
    a = 0
    sum = 0
    while a < number:
        if a%3 == 0 or a%5 == 0:
            sum += a
        a = a+1    
    print (sum)
SumMultiple3or5(input("Enter the limit :"))
