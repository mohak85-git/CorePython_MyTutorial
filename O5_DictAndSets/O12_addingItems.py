numbers = set()  # creates an empty set by calling set constructor
print(numbers, type(numbers))

numbers.add(1)
print(numbers)

data = ['blue', 'red', "blue", 'green', 'red', 'blue', 'white']

# Create a set from the list, to remove duplicates.
unique_data = set(data)
print(unique_data)

# Create a set from the list, to remove duplicates and sort the data
unique_data = sorted(set(data))
print(unique_data)

# Create a list of unique colours, keeping the order they appeared
# unique_data = dict.fromkeys(data)   # Create a dictionary and retain the order
# print(unique_data)
# output: {'blue': None, 'red': None, 'green': None, 'white': None}
unique_data = list(dict.fromkeys(data))
print(unique_data)
# output: ['blue', 'red', 'green', 'white']
