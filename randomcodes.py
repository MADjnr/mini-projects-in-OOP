'''
while True:
    response = input('say something: ')
    if (response == 'nothing'):
        break
'''

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,0,1],
    [0,0,0,0,1,0,0],
    [0,0,0,1,0,0,0]
]

##iterate over picture,
    #if 0 -> print ' '
    #if 1 -> print *
'''
for row in picture:
    for pixel in row:
        if (pixel == 1):
            print('*', end= '')
        else:
            print(' ', end= '')
    print('')
'''

##this is an exercise to print duplicates in list:
some_list = ['a', 'b', 'c', 'b','d','m','n','n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)