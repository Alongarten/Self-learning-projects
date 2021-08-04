import random

print("What is your name?")
name = input().capitalize()
secretnumber = random.randint(1,20)
print("Well, " + name + ", guess a number between 1 to 20")

for guessestaken in range(1,7):
    guess = input()
    try:
        if int(guess) < secretnumber:
            print("Guess higher.")
        elif int(guess) > secretnumber:
            print("Guess lower.")
        else:
            break
    except ValueError or TypeError:
        print('Thats not a valid asnwer')

if int(guess) == secretnumber:
    print("Good job, " + name + ", you guessed the number within " + str(guessestaken) + " tries")

else:
    print("Sorry, the number was " + str(secretnumber))