#No method is needed to iterate over a dictionary: 
d = {'A': 'Apple', 'B': 'Ball', 'C': 'Cat'}

for Key in d:
        print(Key)

#But it's possible to use the method iterkeys(): 
for key in d.iterkeys():
        print(key)

#The method itervalues() is a convenient way for iterating directly over the values:        
for val in d.itervalues():
        print(val)
    
#The above loop is of course equivalent to the following one:    
for key in d:
        print(d[key])

