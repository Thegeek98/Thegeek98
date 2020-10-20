while True:
    print('Who are you?')
    name = input()
    if name != ('Zin KO'):
        continue
    print('Hello, Zin. What is the password? (It is a fish.)')
    password = ' '
    while password != 'swordfish':
        password = input()
        print('Sorry Try Again!')
    print('Access granted.')
    break
print("Your Wellcome! Zin")
