year = input("what year was this book first printed?")
century = year[:2]
dec_number = year[2:3]
print(dec_number)
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