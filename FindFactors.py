# Python program to find factors of a given number and find whether the factor is even or odd

# This function computes the factor of the number passed
def print_factors(x):
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
            even_odd(i)


# This function finds whether the factor is even or odd
def even_odd(i):
    mod = i % 2
    if mod > 0:
        print("Factor", i, "is an odd number.")
    else:
        print("Factor", i, "is an even number.")


num = int(input("Enter a number: "))
print_factors(num)
