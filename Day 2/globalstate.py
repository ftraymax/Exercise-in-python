def spam():
    global eggs
    egg = 'spam'
def bacon():
    eggs = 'bacon'
def ham():
    print(eggs)

eggs = 23
ham()
print(eggs)