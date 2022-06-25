import random


##allows play to enter 7 numbers
ticket= []
for tickets in range(0,7):
    ticket_numbers = int((input('Please enter your number')))
    ticket.append(ticket_numbers)

print('Your numbers are: {}'.format(ticket))

##creates random 7 lottery numbers
lottery= []
for num in range(0,7):
    numbers = random.randint(1,50)
    while numbers in lottery:
        numbers = random.randint(1,50)
    lottery.append(numbers)
print('The lottery numbers are: {}'.format(lottery))

## comparing the 2 tickets
matches=[]
for matches_a in lottery:
    for matches_b in ticket:
        if matches_a == matches_b:
            matches.append(matches_a)

# print('There were {} matches'.format(matches))

## working out what the player has won
print('There were {} matches'.format(len(matches)))
if (len(matches)) == 3:
    print('You matched two numbers and win £20')
elif (len(matches)) == 4:
    print('You matched four numbers and win £40')
elif (len(matches)) == 5:
    print('You matched five numbers and win £100')
elif (len(matches)) == 6:
    print('You matched six numbers and win £10,000')
elif (len(matches)) == 7:
    print('Wow you matched all seven numbers and win the jackpot of £1,000,000!!')
else:
    print('Sorry you did not win today')