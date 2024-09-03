"""Day 23 - List intersection
Write a function to find the intersection of two lists.
"""

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

for i in list1:
    if i in list2:
        print (i)