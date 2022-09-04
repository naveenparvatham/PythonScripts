# Program which accepts a string from console and print it in reverse order
def rev_string(x):
    return x[::-1]


input_string = input("Enter String: ")
reverse_string = rev_string(input_string)
print("Entered String:", input_string)
print("Reverse String:", reverse_string)
