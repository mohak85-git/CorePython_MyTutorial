import random

highest = 15
answer = random.randint(1, highest)
print(f"answer is: {answer}")  # TODO: remove this line after testing
print(f"Please guess number between 1 and {highest}: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:   # guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")
