def Squares(x): return x*x

def pythograstriad(n):
    for x in range(1, n-1):
        for y in range(x+1, n):
            for z in range(y+1, n+1):
                if Squares(z) == Squares(x) + Squares(y):
                   print (x, y, z)
    return False

n = int(input("enter a limit: "))
pythograstriad(n)
