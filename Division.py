# lst = [i for i in range(2000, 3200) if i % 7 == 0 and i % 5 != 0]
# print(lst)

# Program which accepts a sequence of comma separated 4 digit binary
# numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence

nums = list(input("Enter a 4 digit binary number : ").split(','))
res = [num for num in nums if not int(num, 2) % 5]
print(res)
