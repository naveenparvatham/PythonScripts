# Program to print the list after removing
# the value 24 in [12,24,35,24,88,120,155]

# lst = [12, 24, 35, 24, 88, 120, 155]
# new_lst = [x for x in lst if x != 24]
# print(new_lst)


# Program to print the list after removing
# the 0th,4th,5th numbers in [12,24,35,70,88,120,155]

# lst = [12, 24, 35, 70, 88, 120, 155]
# lst = [x for (i, x) in enumerate(lst) if i not in (0, 4, 5)]
# print(lst)

# Program to print the list after removing
# numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]

# lst = [12, 24, 35, 70, 88, 120, 155]
# lst = [x for (i, x) in enumerate(lst) if x % 5 != 0 and x % 7 != 0]
# print(lst)

# Program to randomly generate a list with 5 numbers, which are
# divisible by 5 and 7 , between 1 and 1000 inclusive

# import random
# print(random.sample([i for i in range(1, 1001) if i % 5 == 0 and i % 7 == 0], 5))

# Program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0)
n = int(input("Enter the number: "))
x = 0
for i in range(1, n + 1):
    x = x + (i / (i + 1))
print("The sum of series is: ", round(x, 2))
