# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 16:17:03 2017

@author: prana
"""

def binary_search(alist, item):
    print("Algorithm started")
    found = False
    import time
    t0 = time.time()
    first = 0
    last = len(alist) - 1
    print(last)
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else :
                first = midpoint + 1
    return found
    

input_list = [1,2,3,4,50,6,7,8]
input_list.sort()
print(input_list)
find_item = 5
result = binary_search(input_list, find_item)
if result == True:
    print("Item found in the list")
else :
    print("Item not found in the list")
    
    
    