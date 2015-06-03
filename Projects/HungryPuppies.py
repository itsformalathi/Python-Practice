# Hungry Puppies Challenge from Reddit
#https://www.reddit.com/r/dailyprogrammer/comments/33ow0c/20150424_challenge_211_hard_hungry_puppies/

from random import randint
import itertools

def ExtractPermutationList(number):
    number_list = list(number)
    perm_list = list(itertools.permutations(number_list, len(number)))
    return perm_list

def Happiness_count(number):
    count = 0
    for i in range(len(number)):
        prev = "0" if i == 0 else number[i-1]
        next = number[i-1] if i == len(number)-1 else number[i+1]
        me = number[i]
        if me < next and me < prev:  
           count += -1
        elif me > next and me > prev:
           count += 1
    return count

def HappinessCount_list(perm_list):
    count_list = []
    for i in perm_list:
        count_list.append(Happiness_count(i))
    return count_list    

def Maximum_Happiness(number):
    perm_list = ExtractPermutationList(number)
    count_list = []
    count_list = HappinessCount_list(perm_list)
    maximum = max(count_list)
    print(maximum)
    dictionary = dict(zip(perm_list, count_list))
    for key in dictionary:
        if dictionary[key] == maximum:
           return key    

def main():
    number = input("input your treat: ")
    number = list(number)
    print(Maximum_Happiness(number))
    
main()
