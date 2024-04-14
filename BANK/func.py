from data_i import *
import json


def check_balance(acc_no, password):
    try:
        for i in data["customers"]:
            if i["acc_num"] == acc_no:
                if i["password"] == password:
                    print("Your account balance is:", i["Balance"])
                    break
                else:
                    raise Exception("Incorrect password. Please try again.")
            else:
                raise Exception("Invalid Account Number")
    except Exception as e:
        print(e)


def cash_withdraw(acc_no, password, amount):
    try:
        for i in data["customers"]:
            if i["acc_num"] == acc_no:
                if i["password"] == password:
                    if int(i["Balance"]) >= amount:
                        balance = int(i["Balance"])
                        new_balance = balance - amount
                        i["Balance"] = new_balance
                        with open("datas.json", "w") as file1:
                            json.dump(data, file1)
                        print(
                            f"Withdrawal successfully.New Balance for {acc_no} is:",
                            i["Balance"],
                        )
                        break
                    else:
                        raise Exception("Insufficient Balance")
                else:
                    raise Exception("Incorrect password. Please try again.")
            else:
                raise Exception("Invalid Account Number")
    except Exception as e:
        print(e)


def cash_deposit(acc_no, password, amount):
    try:
        for i in data["customers"]:
            if i["acc_num"] == acc_no:
                if i["password"] == password:
                    if int(i["Balance"]) >= amount:
                        balance = int(i["Balance"])
                        new_balance = balance + amount
                        i["Balance"] = new_balance
                        with open("datas.json", "w") as file1:
                            json.dump(data, file1)
                        print(
                            f"Amount Credited successfully.New Balance for {acc_no} is:",
                            i["Balance"],
                        )
                        break
                    else:
                        raise Exception("Insufficient Balance")
                else:
                    raise Exception("Incorrect password. Please try again.")
            else:
                raise Exception("Invalid Account Number")
    except Exception as e:
        print(e)
