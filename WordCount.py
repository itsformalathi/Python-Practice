

Text = input("Enter some text: ")
dic = {}
for word in Text.split():
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
for Key in dic:        
    print(Key, dic[Key])        
