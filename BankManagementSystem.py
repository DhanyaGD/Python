import random
import Database


class Account(object):

    def createaccount(self):
        print("\n-------------Open an account (0)-------------")
        name = input("Please enter your name:")
        dob = input("Please enter you date of birth: ")
        address = input("Please enter your address:")
        phone = input("Please enter your phone number:")
        balance = input("Please enter the amount you would like to deposit: ")
        account_number = random.randrange(99999)
        print("Welcome " + name + " your account number is", account_number)
        password = set_password(self)
        if password == -1:
            print("Create failed!")
            print("About to return to the main interface!")
            return -1
        print("Password created successfully for your account number: ", account_number)
        Database.createaccount(name, account_number, dob, address, phone, balance, password)

    def depositamount(self):
        account_number = input("Enter the account number: ")
        amount = input("Enter the amount you want to deposit: ")
        Database.deposit(amount, account_number)

    def withdrawamount(self):
        account_number = input("Enter the account number: ")
        amount = input("Enter the amount you want to withdraw: ")
        Database.withdraw(amount, account_number)

    def balanceenquiry(self):
        account_number = input("Enter the account number: ")
        Database.balance(account_number)


def set_password(self):
    for i in range(4):
        password1 = input("please enter your password:")
        password2 = input("Please enter your password again:")
        if password1 == password2:
            return password1
        if i == 3:
            return -1
        print("Sorry, the two passwords you entered do not match, please re-enter!")
