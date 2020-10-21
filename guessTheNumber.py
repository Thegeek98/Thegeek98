# This is a guess number game.
import random
secretnumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretnumber:
        print('Your guess is too low.')
    elif guess > secretnumber:
        print('Your gess is too high.')
    else:
        break # This condition is the correct guess!
if guess == secretnumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + 'guess!')
else:
    print('Nope. The number I was thinking of was ' + str(secretnumber))
