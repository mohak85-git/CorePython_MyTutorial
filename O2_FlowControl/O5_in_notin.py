# in operator
parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print(f"{letter} is in {parrot}")
else:
    print("I don't need that letter")


# not in operator
activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")
