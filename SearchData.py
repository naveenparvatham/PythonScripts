company_data = ['Naveen', '123', 'USA', 'Vasu', '234', 'Hyd']
item = input("Enter the data you want to search for: ")

for i in range(1):
    if item in company_data:
        print("It is available.")
        break
    else:
        print("It is not available.")
