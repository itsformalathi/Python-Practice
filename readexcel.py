import os, math, xlrd, pickle

def Ratio(data1, data2):
    """returns ratio of 2 given items """
    ratio = 0.00
    ratio = data1/ data2
    return ratio

def Ratiolist(list1, list2):
    """ returns a list of ratio's to perform operations later"""
    ratiolist = []
    for r in range(len(list1)):
       # print (list1[r], list2[r])
       # input("enter")
        ratiolist.append(Ratio(list1[r], list2[r]))
    return ratiolist

def Maximum(data):
    """ returns the maximum vaue from a list"""
    maximum = max(data)
    return maximum

def Minimum(data):
    """returns the minimum value from a list"""
    minimum = min(data)
    return minimum

def MaximumRowvalue(ratiolist):
    """returns a row value which holds the maximum value of a given list"""
    row = 0
    maximumratio = Maximum(ratiolist)
    for r in range(len(ratiolist)):
        if maximumratio == ratiolist[r]:
           row = r 
    return row

def Location(value):
    """returns the location details of a given value"""
    return (list_place[val])

def RowMaximumftomRatio(list_female, list_male):
    """ returns the row value which holds the maximum of female to male employment ratio""" 
    return MaximumRowvalue((Ratiolist(list_female, list_male)))

def PoepskRatio(location, list_place, list_poepsk, list_Tnepsk):
    """ returns the ratio of privately owned establishmnets to total number of eatblishments in a given location"""
    for p in range(len(list_place)):
        if list_place[p] == location:
           return Ratio(list_poepsk[p], list_Tnepsk[p])

def ExtractdatafromExcel(filename):
    """Extracts data from Excel file"""
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    data = [[sheet.cell_value(r,c)for c in range(12,sheet.ncols)] for r in range(19, (sheet.nrows-4))]
    return data

def GetData(filename, pickle_file):
    if os.path.isfile(pickle_file): 
        with open (pickle_file, 'rb') as f: 
             data1 = pickle.load(f)
    else:
        with open('my_pickle', 'wb') as f:
           data1 = ExtractdatafromExcel(filename)
           data1 = PreprocessedData(data1)
           dic = pickle.dump(data1, f)
    return data1       

""" Defining data structures required """    

def PreprocessedData(data1):
    data1 = ExtractdatafromExcel(filename)
    transposed = [[row[idx] for row in data1] for idx in range(len(data1[0]))]
         
    list_place = transposed[0]
    list_establishments = transposed[1]
    list_male = transposed[3]
    list_female = transposed[4]
    list_Tnepsk = transposed[6]
    list_Tpepsk = transposed[7]
    list_poepsk = transposed[-2]
    list_popepsk = transposed[-1]
    
    return list_place, list_establishments, list_male, list_female, list_Tnepsk, list_Tpepsk, list_poepsk, list_popepsk

""" Analasying the collected data """

filename = "/home/malathi/Downloads/a001.xls"
pickle_file = "my_pickle"

def main():
    data1 = GetData(filename, pickle_file)
    list_place, list_establishments, list_male, list_female, list_Tnepsk, list_Tpepsk, list_poepsk, list_popepsk = PreprocessedData(data1)
    dic = {0: list_place, 1: list_establishments, 2: list_male,3: list_female, 4: list_Tnepsk, 5: list_Tpepsk, 6: list_poepsk, 7: list_popepsk}
    
    row = RowMaximumftomRatio(list_female, list_male)
    print("The place with highest female to male employment ratio is ", dic[0][row])
    
    location = input("choose a location")
    print("The ratio of privately owned establishments per square kilometre to total number of establishmnets of given location is ", PoepskRatio(location, list_place, list_poepsk, list_Tnepsk))

main()
