import csv

# Open the file in read mode
filename = open('bank-data.csv', 'r')

# Creating dictreader object
file = csv.DictReader(filename)

# Creating empty lists
name = []
age = []
profession = []
phone = []

# Iterating over each row and append values to empty list
for col in file:
    name.append(col['name'])
    age.append(col['age'])
    profession.append(col['profession'])
    phone.append(col['phone'])

    prof_input = input("Enter Profession: ")

    while prof_input != '':
        if prof_input == 'END':
            exit(0)
        elif prof_input.lower() == 'developer':
            print("Client is eligible.")
            print(col['name'], ",", col['age'], ",", col['profession'], ",", col['phone'])
            break
        else:
            print("Client is not eligible.")
            break
