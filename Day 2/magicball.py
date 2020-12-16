import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'it is certain'
    elif answerNumber == 2:
        return 'good day'
    elif answerNumber == 3:
        return 'happy nightmare'
    elif answerNumber == 4:
        return 'yes'
    elif answerNumber == 5:
        return 'hola'
    elif answerNumber == 6:
        return 'jezz'

print(getAnswer(random.randint(1, 9)))