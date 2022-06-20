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







