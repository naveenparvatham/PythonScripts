# Program to print this list after removing all duplicate values
# with original order reserved

def remove(x):
    final_list = []
    for num in x:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Reversing a list using slicing technique
def reverse(lst):
    new_lst = lst[::-1]
    return new_lst


duplicate = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique = remove(duplicate)
print("Unique List:", unique)
print("Reverse of Unique List:", reverse(unique))

