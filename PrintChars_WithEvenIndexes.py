# Program to accept a string from console
# and print characters that have even indexes

input_string = input("Enter a String: ")

if input_string:
    string = ""
    for i in input_string:
        if input_string.index(i) % 2 == 0:
            string += str(i)

    print("Input:", input_string)
    print("Output:", string)
