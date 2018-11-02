name = ''
while not name:
    print('What is your name?')
    name = input()
print('And how many guest will you have?')
numberOfGuest = int(input())
if numberOfGuest:
    print('Be sure to have enough room for all your guests.')
print('Done')