import random

highest = 10
answer = random.randint(1, highest)
print(f"answer is: {answer}")  # TODO: remove this line after testing
print(f"Please guess number between 1 and {highest}: ")
# guess = int(input())

# while True:
#     if guess < answer:
#         guess = int(input("Please guess higher: "))
#         continue
#     elif guess > answer: 
#         guess = int(input("Please guess lower: "))
#         continue
#     else:
#         print("Well done, you guessed it")
#         break

guess = 0
while guess != answer:
    guess = int(input())
    if guess < answer:
        print("Please guess higher: ")
    elif guess > answer:
        print("Please guess lower: ")
    else:
        print("Well done, you guessed it")
