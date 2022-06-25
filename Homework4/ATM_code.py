#1.Pin code an int range 1 to 9999
#2 Pin code exists on file
#3 account balanance = 100.
#4 withdrawal amount le to balance
#5 balance - withdrawl > 0

#1
def is_valid_pin(num,_min, _max):
    if _min <= num <= _max:
        return True
    return False

#3
def is_val_bal(num):
    return num  == 100

#4
def is_valid_amount(amt,bal):
    if amt < bal :
        return True
    return False
#5
def bal_not_neg(bal,amt):
    if bal- amt !=0:
        return True
    return False


#2
def get_file_content(file_name):
    """
    Read content of a file
    :param file_name: str file name or path
    :return: list of str where each str is a line

    Example return:
        [
            '1. line',
            '2. line',
            '3. line',
        ]
    """
    with open(file_name, 'r') as file:
        return file.readlines()


def valid_pin_number(file_name,pin):
    content = get_file_content(file_name)
    for element in content:
        if pin in element:
            return True
    return False



