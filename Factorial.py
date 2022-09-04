def recur_factorial(x):
    if x == 1:
        return 1
    else:
        return x * recur_factorial(x - 1)


num = int(input("Enter number: "))

print("The factorial of", num, "is", recur_factorial(num))
