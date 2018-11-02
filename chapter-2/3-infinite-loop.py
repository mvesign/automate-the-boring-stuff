while True:
    print('What is your name?')
    name = input()
    if name == 'Alice':
        break
    print('That is not correct, try it again.')
print('Great! Thank you, ' + name + '!')