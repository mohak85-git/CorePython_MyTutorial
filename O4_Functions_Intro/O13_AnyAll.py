entries = [1, 2, 3, 4, 5]

print(f"all: {all(entries)}")
print(f"any: {any(entries)}")

print("Iterable with a 'False' value")
entries_with_zero = [1, 2, 0, 4, 5]

print(f"all: {all(entries_with_zero)}")
print(f"any: {any(entries_with_zero)}")

print("Empty iterable")
entries = []
print(f"all: {all(entries)}")
print(f"any: {any(entries)}")

# The all() function returns True if all items in an iterable are true,
# otherwise it returns False. If the iterable object is empty, the all()
# function also returns True.

# The any() function returns True if any item in an iterable are true, otherwise
# it returns False. If the iterable object is empty, the any() function will
# return False.
