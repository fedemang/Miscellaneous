# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:55:39 2020

@author: Federico
"""
#foodict = {k: v for k, v in mydict.items() if k.startswith('foo')}
#from collections import defaultdict
from collections import Counter
from statistics import mode



"""
takes an input list and returns two lists: one with the unique elements, the other with the rest of them
"""

def unique_elements(listin):
    dict1 = Counter(listin) 
    dict2 = dict((key,value) for key, value in dict1.items() if value == 1)
    list1 = list(dict2)
    list2 = [x for x in mylist if x not in list1]
    return list1, list2


#mylist = ["a", "b", "a", "c", "c", "c", "a", "d"]

#un = unique_elements(mylist)
#print(un)
    
"""
returns the nth most abundant element of a input list 
"""

def nth_element(listin, n):
    
    #most_common = mode(dict1.values())
    dict1 = Counter(listin)
    dict2 = Counter(listin)
    for i in range (0, n):
        nth = max(dict1, key = dict1.get)
        del dict1[nth]
    return dict2, nth

mylist = [10, 4, 45, 2, 2, 10, 10, 5, 6, 8, 8, 5, 3, 5, 2, 10]
#mylist = ["a", "b", "a", "c", "c", "c", "a", "a", "d"]

un = nth_element(mylist, 5)
print(un)


#mylist = list(dict.fromkeys(mylist))
#print(mylist)
