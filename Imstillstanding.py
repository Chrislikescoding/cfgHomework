import os
from os.path import exists,join
mylines=[]

song_lines = ['You could never know what its like',
    'Your blood like winter freezes just like ice',
    'And there\'s a cold lonely light that shines from you',
    'You\'ll wind up like the wreck you hide behind that mask you use',
    'And did you think this fool could never win?',
    'Well look at me, Im coming back again',
    'I got a taste of love in a simple way',
    'And if you need to know while I\'m still standing, you just fade away',
    'Dont you know I\'m still standing better than I ever did',
    'Looking like a true survivor, feeling like a little kid',
    'I\'m still standing after all this time',
    'Picking up the pieces of my life without you on my mind',
    'I\'m still standing (Yeah, yeah, yeah)',
    'I\'m still standing (Yeah, yeah, yeah)']

file_name = 'song.txt'

with open(file_name,'w+') as text_file:
        text_file.write('\n'.join(song_lines))

text_file.close()

# get the file path and name using the os module and then check if it exists
path = os.getcwd()
path: str=join(path, 'song.txt')

if exists(path):
    print((file_name) + ' was created in ' + path)
else:
    print(str(path) + ' was NOT created')


with open('song.txt','r+') as outfile:
        for line in outfile:
             if 'still' in line:
                 index= line[:-1]
                 mylines.append(index)

print(mylines)

