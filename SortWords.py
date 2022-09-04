# Program to accept a sequence of words as input and prints the words in a
# sequence after sorting them alphabetically

# To take input from the user
my_str = input("Enter a string: ")

# Split the string into a list of words
words = [word.lower() for word in my_str.split()]

# Sort the list alphabetically
words.sort()

# Display the sorted words
print("The sorted words are:")
for word in words:
    print(word)
