def overlapping(list1, list2):
    return bool(set(list1) & set(list2))
print(overlapping([1, 2, 3], [4, 5, 3]))  
print(overlapping([1, 2], [3, 4]))        
