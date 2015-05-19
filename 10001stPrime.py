def main():
    print (Primenumber()) 

def Isprime(n):
    assert n % 2 != 0
    for i in range(3, n//2, 2):
        if n % i == 0: 
           return False
    return True    

def Primenumber():
    num = 1
    count = 1
    while count < 10001:
          num += 2
          if Isprime(num):
             count += 1
    return (count, num)

if __name__ == "__main__":
    main()
