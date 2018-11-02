print('What is your name?')
name = input()
print('And how old are you?')
age = int(input())
if name == 'Alice' and age >= 12:
    print('Hi, ' + name + '.')
elif  age < 12:
    print('Aren''t you a little young to be Alice?')
else:
    print('You are neither Alice nor a little kid.')