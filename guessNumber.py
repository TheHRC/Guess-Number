# This is a guess the number game.
import random

print("Hello! What is your name? ")
name = input()

print('Well, ' +  name + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)


count = 8
for guessesTaken in range(1,7):
    print("You have {} chances to guess!\nTake a guess: ".format(count-1))
    guess = 0
    try:
        guess = int(input())

    except ValueError:
        print("Invalid input! And you've also lost one chance!")


    if guess < secretNumber:
        print("Your guess is too low!")
    elif guess > secretNumber:
        print("Your guess is too high!")
    else:
        break # This condition is for the correct guess!
    count -=1
if guess == secretNumber:
    print('Good job! ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope! The nubmer I was thinking of was ' + str(secretNumber))
