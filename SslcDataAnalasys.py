import csv
""" 1. Does governament school children performed better in languages or other subjects
    2. is there any regionwise dependency on how students opting for languages 
    3. In which subject blind kids performing better """ 

def ExtractData(filename):
    with open(filename) as csvfile:
        filereader = csv.reader(csvfile, delimiter =';')
        for line in filereader:
            print (line)
            #data = list(filereader)
    #return data

def Getchoice():
    print("what do you want to know?")
    print("1.The average pass percenatge for a desired district")
    print("2. The districts ranking order highest pass percentage wise")
    print("3. The districts ranking order grade wise:")
    print ()
    choice = int(input("Enter your choice: "))
    return choice

def CallOperation(ch):
    if ch == 1:
       #result = DistrictAveragePassPercentage()
       return result
    elif ch == 2:
       #result = PaasPercenatgeDistrictRankingOrder()
       return result
    elif ch == 3:
       #result = GradeDistrictRankingOrder()
       return result
    else:
       print ("Choose among the given options")

file = "/home/malathi/Downloads/cleaned_sslc_data.csv"

def main():       
    #choice = Getchoice()
    #result = CallOperation(choice)
    #print(result)
    ExtractData(file)
main()
