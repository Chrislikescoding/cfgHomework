# for testing purposes this get_pin has only one go at get_pin
class BlankInputError(Exception):
    pass

def get_pin():
 try:
    pin_no = int(input("enter your pin code please "))
    if not pin_no:
        raise BlankInputError
 except BlankInputError as b:
     print(b)
 else:
     return pin_no


def check_pin(pin_no):
    file_object = 'clients.txt'
    with open(file_object, 'r+') as outfile:
        for line in outfile:
            if pin_no == line[-5:-1]:
                return True
    return False

def check_less_than_balance_values(withdrawal_amount):
    balance = 100
    if withdrawal_amount < balance:
        return True
    return False

def check_multiple_of_ten(withdrawal_amount):
    if withdrawal_amount % 10 ==0:
        return True
    return False

def get_bal(withdrawal_amount):
    is_zero=False
    balance = 100
    print(balance)
    is_zero = balance - withdrawal_amount == 0
    return is_zero



