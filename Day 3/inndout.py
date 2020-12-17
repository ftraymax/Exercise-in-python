dogs = ['artyom', 'oreo', 'cheesecake']
print('enter a name')
name = input()
if name not in dogs:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')