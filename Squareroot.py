import math

numbers = input("Enter D: ")
numbers = numbers.split(',')

lst = []
for D in numbers:
    Q = round(math.sqrt((2 * 50 * int(D)) / 30))
    lst.append(Q)

print(lst)
