name = ''
print('What is your name?')
while name != 'Alice':
    name = input()
    if name == 'Alice':
        break
    print('That is not correct, try it again.')
print('Great! Thank you, ' + name + '!')