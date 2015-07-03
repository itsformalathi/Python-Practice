# Hungry Puppies Challenge from Reddit
#https://www.reddit.com/r/dailyprogrammer/comments/33ow0c/20150424_challenge_211_hard_hungry_puppies/

from random import randint
import itertools, sys

def GeneratePermutationList(number):
    """ generates and returns permuttaion list from the given input treat"""
    number_list = list(number)
    perm_list = list(itertools.permutations(number_list, len(number)))
    return perm_list

def Happiness_count(number):
    """ clculates the Happiness count based on the condition that 
    If a puppy receives a bigger treat than both its neighbors do, it is happy (+1 happiness).
    If a puppy receives a smaller treat than both its neighbors do, it is sad (-1 happiness).
    If a puppy does not fit in either of the above categories, it is merely content. This means any puppy with at least one neighbor with the same size treat, or any puppy with one neighbor with a bigger treat and one with a smaller treat.
"""
    count = 0
    for i in range(len(number)):
        prev = "0" if i == 0 else number[i-1]
        next = number[i-1] if i == len(number)-1 else number[i+1]
        me = number[i]
        if me < next < prev:  
           count += -1
        elif me > next > prev:
           count += 1
        """ if me < next and me < prev:
             count += -1
           elif me > next and me > prev:
             count += 1 """
    return count

def HappinessCount_list(perm_list):
    """ calculates the happiness count for each order of numbers from permutation list """
    count_list = []
    for i in perm_list:
        count_list.append(Happiness_count(i))
    return count_list    

def Maximum_Happiness(number):
    """ extracts & returns the maximum hapiness & the respective rearranged order of numbers 
        from given input """ 
    perm_list = GeneratePermutationList(number)
    count_list = []
    count_list = HappinessCount_list(perm_list)
    maximum = max(count_list)
    print(maximum)
    dictionary = dict(zip(perm_list, count_list))
    for key in dictionary:
        if dictionary[key] == maximum:
           return key    

def main():
    number = sys.argv[1]
    number = list(number)
    print(Maximum_Happiness(number))
    
main()

