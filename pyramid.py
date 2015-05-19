import sys
 
"""limit = int(sys.argv[1])
width = int(sys.argv[2])"""

def pyramid(limit, width):
    space = " "
    star = "*"
    for i in range(1, limit+1):
       line = ""
       line += (width//2 - i) * space
       line += (2*i - 1) * star
    print (line) 

pyramid(int(sys.argv[1]), int(sys.argv[2]))
