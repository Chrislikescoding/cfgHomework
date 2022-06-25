try:
    file_object = open('people.txt', 'r')
except FileNotFoundError as f:
    print('This file is not found')
else:
    print('This file is found')
    file_object.close()
finally:
    print('I hope this is right')
