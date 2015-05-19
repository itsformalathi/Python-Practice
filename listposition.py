# Getting the position of different elements in a list
list1 = [1,2,3,4]
list2 = ['one','two','three','four']
for index, s in enumerate(list1):
    print (index, s)

# Getting the position of ith element in a list
print (list1.index(4))

# Getting the position of ith element in a list based on meeting a condition
[print(i) for i,x in enumerate(list1) if x == 3]

# sequencing through multiple lits
for q, a in zip(list1, list2):
    print ('{0} is {1}.'.format(q, a))
