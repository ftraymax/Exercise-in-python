cat = []
while True:
    print('enter the name of the cat ' + str(len(cat) + 1) + ' or do not enter anything to stop')
    name = input()
    if name == '':
        break
    cat = cat + [name]
print('the cat names are')
for name in cat:
    print(name)

