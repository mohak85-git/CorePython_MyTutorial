low = 1
high = 1000
count = 0

print(f"Please think of a number between {low} and {high}.")
input("Press ENTER to start. ")

# while True:
while low != high:
    count += 1
    guess = low + ((high - low) // 2)
    hi_lo = input(f"My guess is {guess}. Should I guess Higher or Lower?\
 Enter h, or l or c if my guess was correct. ").casefold()
    if hi_lo == 'h':
        low = guess + 1
    elif hi_lo == 'l':
        high = guess - 1
    elif hi_lo == 'c':
        print(f"I got it right in {count} guesses!")
        break
    else:
        print("Enter h, or l or c only. ")
else:
    count += 1
    print(f"You thought of the number {low}")
    print(f"I got it in {count} guesses!")
