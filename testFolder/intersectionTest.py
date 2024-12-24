import numpy as np

def check_intersection(list1, list2):
    # convert the lits of coordinates into numpy arrays
    arr1 = list1
    arr2 = list2
    
    # check if the two arrays intersect by finding the minimum and maximum x and y values
    min_x1, min_y1 = arr1.min(axis=0)
    max_x1, max_y1 = arr1.max(axis=0)
    min_x2, min_y2 = arr2.min(axis=0)
    max_x2, max_y2 = arr2.max(axis=0)
    
    # return True if the arrays intersect, False otherwise
    return (min_x1 <= max_x2 and min_x2 <= max_x1) and (min_y1 <= max_y2 and min_y2 <= max_y1)
    
# example usage
list1 = [(0,0), (1,1), (1,0), (0,1)]
list2 = [(2,2), (3,3), (3,2), (2,3)]

print(check_intersection(list1, list2))# returns False
