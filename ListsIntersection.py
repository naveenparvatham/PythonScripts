# Program to make a list whose elements are intersection of the above given lists
def intersection(x1, x2):
    return set(x1).intersection(x2)


lst1 = [1, 3, 6, 78, 35, 55]
lst2 = [12, 24, 35, 24, 88, 120, 155]
print(intersection(lst1, lst2))
