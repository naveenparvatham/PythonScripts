# For loop that prints all elements of a list and their position in the list
a = [4, 7, 3, 2, 5, 9]
print(a)
for i in a:
    print("Element: " + str(i) + " Index: " + str(a.index(i)))
