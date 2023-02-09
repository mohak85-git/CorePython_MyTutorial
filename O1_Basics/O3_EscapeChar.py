splitString = "This string has been \nsplit over\nseveral\nlines."
print(splitString)
print()

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)
print()

print('The pet shop owner said "No, no, \'e \'s uh,...he\'s resting".')
print("The pet shop owner said 'No, no, \'e \'s uh,...he\'s resting'.")
# In this case, use escape char (\ or backslash) to have quotes (double or single) as part of string.

print("""The pet shop owner said "No, no, \'e \'s uh,...he\'s resting".""")
# A pair of 3 quotes (single or double) are called as Docstrings.

print()

anotherString = """This string has been
split over
several
lines."""

print(anotherString)

anotherString = """This string has been \
split over \
several \
lines."""
# While working with extremely long strings use backslash to indicate python about string continuation.

print(anotherString)
print()

# How to include backslash character inside a string?
print("C:\\Users\\timbuchalka\\notes.txt")  # preferred
# or
print(r"C:\Users\timbuchalka\notes.txt")  # r => raw strings
