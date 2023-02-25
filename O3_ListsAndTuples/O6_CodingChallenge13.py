# Adding items to lists

# We have some data that contains a mixture of flowers and shrubs, in a list.
# Our customer would like two separate lists.
# One, called flowers, will contain only flowers, and the other, not 
# surprisingly called shrubs, must contain only shrubs.

# Write code to populate the two lists with the appropriate plants from data.
# The strings in the lists should remain unchanged.
# If you decide to delete " - Flower" and " - Shrub" from the strings, that's 
# a great improvement but isn't required to complete this exercise. But be 
# warned, the on-line checker will fail your code if you attempt to delete 
# those redundant characters but leave a trailing space in the strings.

# Write your code below the comment, starting on line 27.

# There is no need to print the lists, but you can if you wish.


data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for item in data:
    if 'flower' in item.casefold():
        flowers.append(item[:-len(" - Flower")])
    else:
        shrubs.append(item[:-len(" - Shrub")])

print("The flowers are:")
for flower in flowers:
    print(f"\t{flower}")

print()

print("The shrubs are:")
for shrub in shrubs:
    print(f"\t{shrub}")
