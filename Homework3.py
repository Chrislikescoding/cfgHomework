# Homework 3
# Task 1
# Question 1
# Create a program that tells you whether or not you need an umbrella when you
# leave the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y' it should output ''Take an umbrella';
# 3. If the input is 'n', it should output 'You don't need an umbrella'

is_raining = input("Is it raining?").lower() == 'y'

if is_raining:
    print("Take your umbrella")
else:
    print("You don't need an umbrella")

# Homework 3
# Task 1
# Question 2

# I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5
# deposit. I've written a program to check that I can afford the cost, but something
# doesn't seem right. Have a look at my program and work out what I've done
# wrong
# used floats to compare and changed < to >

#Answer
# I just used float to compare the numeric value and changed < to > because it was the wrong way round.

my_money = float(input('How much money do you have? '))
boat_cost = 20 + 5
if my_money > float(boat_cost):
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')

# Homework 3
# Task 1
# Question 3
# Your friend works for an antique book shop that sells books between 1800 and
# 1950 and wants to quickly categorise books by the century and decade that they
# were written. Write a program that takes a year (e.g. 1872) and outputs the
# century and decade (e.g. 'Eighteenth Century, Seventies')


year = input("what year was this book first printed?")
century = year[:2]
dec_number = year[2:3]

decade = ' '
if century == '19':
  word = 'Twentieth '
elif century == '18':
  word = 'Nineteenth '

if dec_number == '0':
  decade = 'Noughties'
elif dec_number == '1':
  decade  = 'Tens'
elif dec_number == '2':
  decade ='Twenties'
elif dec_number == '3':
  decade ='Thirties'
elif dec_number == '4':
   decade ='Forties'
elif dec_number == '5':
    decade = 'Fifties'
elif dec_number == '6':
     decade ='Sixties'
elif dec_number == '7':
  decade ='Seventies'
elif dec_number == '8':
 decade = 'Eighties'
elif dec_number == '9':
  decade ='Nineties'

print(f'{word}century,{decade} ')



#Homework 3
# Task 2
# Question 1 first element should be element 0 not 1

shopping_list = [
'oranges',
'cat food',
'sponge cake',
'long-grain rice',
'cheese board',
]
print(shopping_list[0])


#Homework 3
# Task2
#Question 2

chocolate = input('Chocolate type: ')

chocolates = {
        'white': '1.50',
        'milk': '1.20',
        'dark': '1.80',
        'vegan': '2.00',
    }

if chocolate == 'white':
    print(chocolates['white'])

elif chocolate == 'milk':
    print(chocolates['milk'])

elif chocolate == 'dark':
    print(chocolates['dark'])

elif chocolate == 'vegan':
    print(chocolates['vegan'])

#homework 3
#task 2
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

#homework 3
#task 3
# question 1
# on word document

#homework 3
#task 3
# question 2
#answer change 'r' to 'w' or r+
poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w') as poem_file:
    poem_file.write(poem)

#homework 3
#task 3
# question 3

import os
from os.path import exists, join

mylines = []

song_lines = ['You could never know what its like',
              'Your blood like winter freezes just like ice',
              'And there\'s a cold lonely light that shines from you',
              'You\'ll wind up like the wreck you hide behind that mask you use',
              'And did you think this fool could never win?',
              'Well look at me, I\'m coming back again',
              'I got a taste of love in a simple way',
              'And if you need to know while I\'m still standing, you just fade away',
              'Dont you know I\'m still standing better than I ever did',
              'Looking like a true survivor, feeling like a little kid',
              'I\'m still standing after all this time',
              'Picking up the pieces of my life without you on my mind',
              'I\'m still standing (Yeah, yeah, yeah)',
              'I\'m still standing (Yeah, yeah, yeah)']

file_name = 'song.txt'

with open(file_name, 'w+') as text_file:
    text_file.write('\n'.join(song_lines))

text_file.close()

# get the file path and name using the os module and then check if it exists
path = os.getcwd()
path: str = join(path, 'song.txt')

if exists(path):
    print((file_name) + ' was created in ' + path)
else:
    print(str(path) + ' was NOT created')

with open('song.txt', 'r+') as outfile:
    for line in outfile:
        if 'still' in line:
            index = line[:-1]
            mylines.append(index)

print(mylines)

#homework 3
# Task 4
#Question 1
import requests
import random

poke_numbers = []

#generate 6 random pokemon numbers

poke_numbers = [random.randint(1, 99) for num in range(6)]
#file name
file_name = 'pokemon.txt'
with open(file_name, 'w') as text_file:
    for pnumber in poke_numbers:
       url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pnumber)
       response = requests.get(url)
       pokemon = response.json()

       text_file.write(pokemon['name'] + ' (pokemon number ' + str(pnumber) + ')'' has these moves :')
       moves = pokemon['moves']
       for move in moves:
          text_file.write('\n' + move['move']['name'])



#homework 3
# Task 4
#Question 2

import requests
from pprint import pprint

url = 'https://opentdb.com/api.php'

parameters = {
    "amount": 10,
    "type": "multiple"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]

pprint(question_data)