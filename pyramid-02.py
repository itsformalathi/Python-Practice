import sys

      
limit = int(sys.argv[1])
width = int(sys.argv[2])
space = " "
star = "*"

for i in range(1, limit+1):
    line = ""
    for j in range(width // 2 - i):
        line += space
    for k in range(2 * i - 1):
        line += star
    print (line) 
