import random

answer = [ 'It so certain', 'It is decidely so', 'without a doubt', 'Yes definitely', 'You may rely on it', 'As i see it', 'Most likely', 'outlook good', 'Your signs point to say yes', 'resply hazy', 'try again', 'Ask again', 'Better not to tell you now','cannot predict now','Concentrate and ask again', 'Don not count on it', 'my reply is no', 'My sources say no', 'Outlook not so look', 'Very doubtful']


print('   ___   ___         __           ________    __________      ________     _______')
print(' |    \ /    |      /  \        /  _______|  |___   ___ |   /   _____ |  /   ___   \ ')
print(' |   \   /   |     /    \      |  |    ___       |  |      |   /        |  /     \  |')
print(' |  | \_/ |  |    /  __  \     |  |   |_  |      |  |      |  |         |  \ ___ /  |  ')
print(' |  |     |  |   /  /__\  \    |  |     | |      |  |      |  |         |  /     \  |   ')
print(' |  |     |  |  /  /    \  \   |  \_____| |   ___|  |___   |   \ _____  |  \ ___ /  |')
print(' |  |     |  | /  /      \  \   \  _______|  | ________ |   \ _______ |  \  ______ / ' )
print(" ")
print(" ")
print("Hello world, Welcome to Magic 8 ball , What's your name ?")
name = input()
print("hello" + name)

def Magicball():
    print("Ask me a question ?")
    input()
    print(answer[random.randint(0, len(answer)-1)])
    print("I hope that Helped !")
    Replay()


def Replay():
    print("Do you want to ask another question?")
    reply = input()
    if reply == 'Y':
         Magicball()
    else:
        quit()

Magicball()


