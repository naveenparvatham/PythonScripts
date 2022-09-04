import csv
from aifc import Error

filename = open('FairDealCustomerData.csv', 'r')
file = csv.DictReader(filename)
name = []
age = []
phone = []


class CustomerNotAllowedException(Error):
    print("This customer is not allowed.")
    pass


def create_order(name1):
    try:
        if name1 != 'ABC0':
            print('Customer is allowed.')
            product_name = input("Enter Product Name: ")
            product_code = input("Enter Product Code: ")
            return product_name
        else:
            raise CustomerNotAllowedException
    finally:
        pass


class customer:
    # Iterating over each row and append values to empty list
    for col in file:
        name.append(col['name'])
        age.append(col['age'])
        phone.append(col['phone'])
        print(col['name'], ",", col['age'], ",", col['phone'])
        create_order(col['name'])
