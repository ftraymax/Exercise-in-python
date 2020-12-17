while True:
    print('who are you')
    name = input()
    if name != 'joe':
        continue
    print('hello,Joe. What is the password')
    password = input()
    if password == 'swordfish':
        print('access granted')
        break
    print('Access denied')