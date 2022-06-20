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