print ("Answer - Q1")

def f(n):
    for x in range(3):
        yield x**3
for x in f(5):
    print (x)

#Q.2 What will be the output of the code below?

list = ['a', 'b', 'c', 'd', 'e']
print("Answer - Q2")
print (list[10:])

""" The above code will output [], and will not result in an IndexError.
As one would expect, attempting to access a member of a list using an index that exceeds the number of members (e.g., attempting to access list[10] in the list above) results in an IndexError. However, attempting to access a slice of a list at a starting index that exceeds the number of members in the list will not result in an IndexError and will simply return an empty list. """

# Q.3 What will be the output of the code below in Python 2? Explain your answer.

def div1(x,y):
    print ("%s/%s = %s" % (x, y, x/y))
            
def div2(x,y):
    print ("%s//%s = %s" % (x, y, x//y))

print("Answer - Q.3")
div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)

# Q.4 What will be the output of the code below? Explain your answer.

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print("Answer - Q4")
print ("list1 = %s" % list1)
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)

""" The output of the above code will be:

    list1 = [10, 'a']
    list2 = [123]
    list3 = [10, 'a']

    Many will mistakenly expect list1 to be equal to [10] and list3 to be equal to ['a'], thinking that the list argument will be set to its default value of [] each time extendList is called.

    However, what actually happens is that the new default list is created only once when the function is defined, and that same list is then used subsequently whenever extendList is invoked without a list argument being specified. This is because expressions in default arguments are calculated when the function is defined, not when it’s called.

    list1 and list3 are therefore operating on the same default list, whereas list2 is operating on a separate list that it created (by passing its own empty list as the value for the list parameter). """

#The definition of the extendList function could be modified as follows, though, to always begin a new list when no list argument is specified, which is more likely to have been the desired behavior: 

def extendList1(val, list=None):
    if list is None:
       list = []
       list.append(val)
    return list

# Q.5 What will be the output of the code below? Explain your answer.

class Parent(object):
        x = 1

class Child1(Parent):
      pass

class Child2(Parent):
      pass

print("Answer - Q5")
print (Parent.x, Child1.x, Child2.x)
Child1.x = 2
print (Parent.x, Child1.x, Child2.x)
Parent.x = 3
print (Parent.x, Child1.x, Child2.x)

""" The output of the above code will be:

    1 1 1
    1 2 1
    3 2 3

    What confuses or surprises many about this is that the last line of output is 3 2 3 rather than 3 2 1. Why does changing the value of Parent.x also change the value of Child2.x, but at the same time not change the value of Child1.x?

    The key to the answer is that, in Python, class variables are internally handled as dictionaries. If a variable name is not found in the dictionary of the current class, the class hierarchy (i.e., its parent classes) are searched until the referenced variable name is found (if the referenced variable name is not found in the class itself or anywhere in its hierarchy, an AttributeError occurs).

    Therefore, setting x = 1 in the Parent class makes the class variable x (with a value of 1) referenceable in that class and any of its children. That’s why the first print statement outputs 1 1 1.

    Subsequently, if any of its child classes overrides that value (for example, when we execute the statement Child1.x = 2), then the value is changed in that child only. That’s why the second print statement outputs 1 2 1.

    Finally, if the value is then changed in the Parent (for example, when we execute the statement Parent.x = 3), that change is reflected also by any children that have not yet overridden the value (which in this case would be Child2). That’s why the third print statement outputs 3 2 3."""

#Q-6 What will be the output of the code below? Explain your answer.

def multipliers():
        return [lambda x : i * x for i in range(4)]

print ("Answer - Q6")
print ([m(2) for m in multipliers()])

#How would you modify the definition of multipliers to produce the presumably desired behavior?

# Q-7 Consider the following code snippet:

print("Anwer - Q7")
list = [ [ ] ] * 5
print(list)  # output?
list[0].append(10)
print(list)  # output?
list[1].append(20)
print(list)  # output?
list.append(30)
print(list)  # output?

# What will be the ouput of lines 2, 4, 6, and 8? Explain your answer.

