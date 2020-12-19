birthday = {'alice': 'may 1', 'bob': 'june 6', 'joe': 'dec 21'}
while True:
    print('enter the the name : (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthday:
        print(birthday[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('what is their birthday')
        bday = input()
        birthday[name] = bday
        print('birthday database updated')