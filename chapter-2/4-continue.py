while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hi, Joe. What is the password?')
    password = input()
    if password == 'bananabread':
        break
print('Access granted')