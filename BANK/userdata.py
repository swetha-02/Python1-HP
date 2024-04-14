from func import *

while True:
    try:
        option = int(
            input(
                "Select any one of the option:\n1.Check Balance\n2.Cash Withdraw\n3.Cash Deposit\n"
            )
        )
        if option == 1:
            acc_no = int(input("Enter the account number:"))
            pwd = input("Enter the password:")
            check_balance(acc_no, pwd)
        elif option == 2:
            acc_no = int(input("Enter the account number:"))
            pwd = input("Enter the password:")
            amount = int(input("Enter the amount to be withdrawn:"))
            cash_withdraw(acc_no, pwd, amount)
        elif option == 3:
            acc_no = int(input("Enter the account number:"))
            pwd = input("Enter the password:")
            amount = int(input("Enter the amount to be deposited:"))
            cash_deposit(acc_no, pwd, amount)
        else:
            raise Exception("Enter valid option")

        con = input("Do you want to continue(Y/N):")
        if con == "n" or con == "N" or con == "0":
            print("Transaction completed")
            break
    except Exception as e:
        print(e)
