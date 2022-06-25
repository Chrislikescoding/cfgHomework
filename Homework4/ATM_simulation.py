import os

# Question 1
# Simple ATM program
# Using exception handling code blocks such as try/ except / else / finally, write a
# program that simulates an ATM machine to withdraw money.
# (NB: the more code blocks the better, but try to use at least two key words e.g.
# try/except)
# I am a bank machine
#
# TASK 2 (Exception Handling)

class ExcessiveWithdrawalAmount(Exception):
    pass
class BlankInputError(Exception):
    pass
class NotMultipleOfTen(Exception):
    pass



def check_pin(pin_no):
    file_object = 'clients.txt'
    try:
        with open(file_object, 'r+') as outfile:
            for line in outfile:
                if pin_no == line[-5:-1]:
                    return True
    except FileNotFoundError as f:
        print('The required client file is not found ')
    else:
        print('program is checking the client data base')
    finally:
        outfile.close()


def get_pin():

    try:
        pin_no = input("enter your pin code please ")

        if not pin_no:
            raise BlankInputError
        else:
            attempts_counter = 0
            print(check_pin(pin_no))
            while attempts_counter < 2:
                attempts_counter += 1
                print(attempts_counter)
                if check_pin(pin_no) != True:
                    pin_no = input("please re-enter your pin ")
                else:
                    return True

    except BlankInputError as b:
        print("Pin number cannot be blank,please enter a PIN"
              "")
    except EOFError as e:
        print("There is an issue with your input, did you enter any?"
              "")
    else:
        print("Checking entered pin number")

def calculate_balance(withdrawal_amount):
    assert (type(withdrawal_amount) == int)
    assert (withdrawal_amount > 0)  # evaluates to True or False and Panic

    balance = 100

    try:
        if   withdrawal_amount > balance:
            raise ExcessiveWithdrawalAmount
        elif (withdrawal_amount % 10 != 0):
            raise NotMultipleOfTen
        elif (balance-withdrawal_amount) <= 0:
            raise ValueError
    except AssertionError as a:
        print ("Withdrawal amount is not in the correct format")
    except ExcessiveWithdrawalAmount as ewd:
        print ("Don't be silly! you can't withdraw more than your balance")
    except NotMultipleOfTen as nmt:
        print ("The amount to withdraw should be a multiple of ten")
    except ValueError as t:
        print(f"balance cannot be zero: {t}")
    except TypeError as t:
            return ("This is a type error")

    else:
        balance -= int(withdrawal_amount)
        print(f'{withdrawal_amount} was withdrawn from your account {balance} remaining')
    finally:
        print(f'Your balance now stands at {balance}')
    return balance

if get_pin() == True:
    try:
        withdrawal_amount = int(input('enter how much you would like to withdraw in multiples of £10? '))
    except ValueError as v:
        print("you must enter a numeric value")
    else:
        calculate_balance(withdrawal_amount)




