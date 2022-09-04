# Python program to create bank account class
# with both a deposit() and a withdraw() function
def change():
    response = input("Do you want to change your password?: ")
    if response.lower() == "yes":
        x = input("Enter new password: ")
        y = input("Confirm password: ")
        if x == y:
            print("Your password has been changed.")
        else:
            print("Passwords did not match. Please try again.")
    else:
        return


class bank_account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to ABC Bank...")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance.")

    def display(self):
        print("\n Net Available Balance=", self.balance)


# Driver code

# creating an object of class
s = bank_account()

# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()
change()
