import random
secretNumber = random.randint(1, 10)
print("I'm thinking of a number btw 1 and 10")
for guessesTaken in range(1, 4):
    print('take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('your guess is low')
    elif guess > secretNumber:
        print('your guess is high')
    else:
        break

if guess == secretNumber:
            print('congrats, you guessed it in ' + str(guessesTaken) + 'guesses')
else:
            print('Sorry. The correct number was '+ str(secretNumber))