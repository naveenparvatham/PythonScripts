# Program to find all the numbers between 1000 and 3000 such that each digit of a number is an even number

even_digits = []
a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))
for x in range(a, b):
    if int(x) % 2 == 0 and int(x) % 20 < 10 and int(x) % 200 < 100 and int(x) % 2000 < 1000:
        even_digits.append(str(x))
print(','.join(even_digits))
