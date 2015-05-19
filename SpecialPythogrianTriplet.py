for a in range(1000):
    for b in range(1000):
        c = 1000-a-b
        if c*c == a*a - b*b:
           print (a * b * c)
