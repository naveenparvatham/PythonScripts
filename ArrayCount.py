# Q(5): How do you Count The Number Of Times Each Value Appears In An Array Of Integers?
def count(a_lst, a_len):
    c_list = []
    for vc in range(a_len):
        r_lst = 0
        for ac in range(a_len):
            if vc == a_lst[ac]:
                r_lst += 1
        c_list.append(r_lst)
    return c_list


arr_list = [0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
arr_len = len(arr_list)
print("List:", arr_list)
print("No. of times:", count(arr_list, arr_len))
