flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]

# for flower in flowers:
#     print(flower)
separator = ", "
output = separator.join(flowers)
print(output)
print(type(output))

print()
print(", ".join(flowers))

# The .join() method works only with strings. it is actually a generator.
# It also iterates over the iterable automatically, we need not explicitly 
# loop over the items.
# It expects all the items of the iterable to be of string type.
# It returns a string.
