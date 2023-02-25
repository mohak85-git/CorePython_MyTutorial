data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]

print(f"Original Data is: {data}")
data.sort()
print(f"Sorted Data is: {data}")
print(f"Reversed sorted Data is: {list(reversed(data))}")
print(f"After reversed() method, Data is: {data}")
data.reverse()
print(f"After reverse() function, Data is: {data}")
