import sys

import mysql.connector
import mysql

mydb = mysql.connector.connect(host='localhost', user='root', password='Ponnu@0103', database='BANK_MANAGEMENT')
cursor = mydb.cursor()


def createaccount(name, account_number, dob, address, contact_number, balance, password):
    sql1 = "INSERT INTO account(name, account_number, date_of_birth, address, contact_number, balance) " \
           "values(%s,%s,%s,%s,%s,%s) "
    sql2 = "insert into amount (name, account_number, balance) values(%s,%s,%s)"
    sql3 = "insert into user(name, password) values(%s,%s)"
    val1 = (name, account_number, dob, address, contact_number, balance)
    val2 = (name, account_number, balance)
    val3 = (name, password)
    cursor.execute(sql1, val1)
    cursor.execute(sql2, val2)
    cursor.execute(sql3, val3)
    mydb.commit()


def deposit(amount, account_number):
    account_balance = "select balance from amount where Account_Number = %s"
    data = (account_number,)
    print(data)
    cursor.execute(account_balance, data)
    result = cursor.fetchone()
    print(result)
    deposited = result[0] + int(amount)
    print(deposited)
    sql1 = "update account set balance = %s where Account_Number = %s"
    sql2 = "update amount set balance = %s where Account_Number = %s"
    val1 = (deposited, account_number)
    val2 = (deposited, account_number)
    cursor.execute(sql1, val1)
    cursor.execute(sql2, val2)
    mydb.commit()


def withdraw(amount, account_number):
    account_balance = "select balance from amount where Account_Number = %s"
    data = (account_number,)
    print(data)
    cursor.execute(account_balance, data)
    result = cursor.fetchone()
    print(result)
    withdrawn = result[0] - int(amount)
    print(withdrawn)
    sql = "update amount set Balance = %s where Account_Number = %s"
    val = (withdrawn, account_number)
    cursor.execute(sql, val)
    mydb.commit()


def balance(account_number):
    account_balance = "select balance from amount where Account_Number = %s"
    data = (account_number,)
    print(data)
    cursor.execute(account_balance, data)
    result = cursor.fetchone()
    print("Your Balance is: ", result[-1])


def login(name, password):
    find_user = "select * from user where name = %s and password = %s"
    cursor.execute(find_user, [name, password])
    result = cursor.fetchone()
    if result:
        for _ in result:
            print("welcome")
    else:
        print("invalid credentials")
        sys.exit()
