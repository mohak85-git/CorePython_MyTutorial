pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
# sorted() creates a new list object and does not alter the original object
print(letters)
print()

numbers = [1.2, 4.4, 3.4, 9.7, 5.3]
numbers.sort()
# the .sort() method works on the original object and alters it, without
# creating a new object.

print(numbers)
print()

letter_uncase = sorted(pangram, key=str.casefold)
print(letter_uncase)
print()

# Similarly, key=str.casefold can be called with .sort()

digits = sorted("43281769")
print(digits)
print()
# Here the output is a list of string.
