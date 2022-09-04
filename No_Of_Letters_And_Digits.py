# Program to accept a sentence and calculate the number of letters and digits.
s = input("Enter a sentence: ")
d = l = 0
for c in s:
    if c.isdigit():
        d = d + 1
    elif c.isalpha():
        l = l + 1
    else:
        pass
print("Letters: ", l)
print("Digits: ", d)
