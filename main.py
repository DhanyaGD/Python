"""A bank management system which provides user login and Admin login access"""
"""A new user can perform tasks such as create a account deposit amount, Withdraw amount, do balance enquiry"""
"""Admin has access to do all of the above said tasks"""
"""The user details are stored into MySQL Database and used for performing operations"""

import sys
from BankManagementSystem import Account
import Database


class Admin:
    def __init__(self, account='admin', password='123456'):
        self.account = account
        self.password = password

    def Login(self):
        for _ in range(3):
            account = input('Please enter the administrator account:')
            password = input('Please enter the administrator password:')

            if account == 'admin' and password == '123456':
                return True
            else:
                print("INVALID CREDENTIALS")
        sys.exit()


class Menu:
    def run(self):
        bank = Account()
        while True:
            print("************Welcome to Bank Management System**************")
            print()
            choice = input("""
                                A: Register
                                B: Login  
                                C: Admin
                                Q: Logout

                                Please enter your choice: """)
            if choice == "A" or choice == "a":
                print("\t\t\t\t\t\tMENU")
                print(""" 
                            1: Create account
                            2: Quit""")
                user_input = input("choose from the above menu: ")
                if user_input == "1":
                    bank.createaccount()
                elif user_input == "2":
                    Menu()
                else:
                    print("INVALID CHOICE Choose between 1-2")
            elif choice == "B" or choice == "b":

                name = input("Please enter your username: ")
                password = input("Please enter your password: ")

                Database.login(name, password)

                print("\t\t\t\t\t\t\t\t\tMENU")
                print("""
                            1: Withdraw Amount
                            2: Deposit Amount   
                            3: Balance Enquiry
                            4: Exit""")
                user_input = input("choose from the above menu: ")
                if user_input == "1":
                    bank.withdrawamount()
                elif user_input == "2":
                    bank.depositamount()
                elif user_input == "3":
                    bank.balanceenquiry()
                elif user_input == "4":
                    Menu()
                else:
                    print("INVALID CHOICE Choose between 1-5")
                    Menu()
            elif choice == "C" or choice == "c":
                adminOps = Admin()
                adminOps.Login()

                print("\t\t\tMENU")
                print("""
                                1: Create account
                                2: Withdraw Amount
                                3: Deposit Amount
                                4: Balance Enquiry
                                5: Exit""")
                user_input = input("choose from the above menu: ")
                if user_input == "1":
                    bank.createaccount()
                elif user_input == "2":
                    bank.withdrawamount()
                elif user_input == "3":
                    bank.depositamount()
                elif user_input == "4":
                    bank.balanceenquiry()
                elif user_input == "5":
                    Menu()
                else:
                    print("INVALID CHOICE Choose between 1-4")
                    Menu()
            elif choice == "Q" or choice == "q":
                sys.exit()
            else:
                print("You must select either A or B")
                print("Please try again")
                Menu()


if __name__ == "__main__":
    Menu().run()
