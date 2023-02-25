even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()   # in this case .copy() is faster than list()
#                                 creates a shallow copy
print(more_numbers)

print(numbers is more_numbers)
print(numbers == more_numbers)

del odd[3:]
print(odd)
