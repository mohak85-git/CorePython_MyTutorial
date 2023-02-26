data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

# print(data)

# Method 1

# for index in range(len(data) -1, -1, -1):
#     print(index)
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]

# Method 2

# top_index = len(data) - 1
# for index, value in enumerate(reversed(data)):
#     # print(index, value)
#     if value < min_valid or value > max_valid:
#         print(top_index - index, value)
#         del data[top_index - index]

# Note: Deleting each item one-by-one is inefficient than deleting a slice of
#       data. Therefore, when possible sort the data, build index and then
#       delete in one shot.

# Method 3

data.sort()
print(data)

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

del data[:stop]

start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break

del data[start:]

print(data)
