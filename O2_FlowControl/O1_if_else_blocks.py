# for i in range(1, 13):
#     print(f"No. {i:>2} squared is {i**2:>3} and cubed is {i**3:>4}")

name = input("Please enter your name: ")
age = int(input(f"How old are you, {name}? "))

if age < 18:
    print(f"Please come back in {18 - age} years")
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
