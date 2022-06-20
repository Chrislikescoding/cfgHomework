# homework 3
# task 2
# question 3
import random
counter = 0
prize = 0
sorry = ''
my_winning_numbers = []


lottery_numbers = random.sample(range(1, 99), 7)

print('\033[91m' + '\033[1m' + "Tonight's winning numbers are: ......" + str(lottery_numbers) + '\033[0m')

is_lucky_dip = input("Would you like a lucky dip y/n?").lower() == 'y'


if is_lucky_dip:
    my_winning_numbers = random.sample(range(1, 99), 7)
else:
    print('Check the lottery numbers on your ticket, you will be prompted for each number')
    for number in range(0, 7):
        my_number = int((input('Please enter number ' + str(number + 1) + ' ')))
        my_winning_numbers.append(my_number)

print("Your numbers are :" + str(my_winning_numbers))

for num in range(7):
    if my_winning_numbers[num] in lottery_numbers:
        counter += 1
    if counter == 3:
        prize = 20
        first_word = 'Well done'
    elif counter == 4:
        prize = 40
        first_word = 'Well done'
    elif counter == 5:
        prize = 1000
        first_word = 'Congratulations!!!'
    elif counter == 6:
        prize = 10000
        first_word = 'Congratulations!!!'
    elif counter == 7:
        prize = 1000000
        first_word = '\033[1m''\033[91m''Congratulations!! You no longer need to learn Python. Buy your instructor a BIG present on the way out!!!'
else:
    if counter in [0, 1, 2]:
       print(counter)
       sorry = 'Sorry '
       first_word = ''

print(f'{first_word} You have {counter} numbers', sep='')
print(f'{sorry}You have won {prize} pounds')
