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
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plants_filename = "flowers_print.txt"
# with open(plants_filename, mode='w') as plants:
#     for plant in data:
#         if 'Flower' in plant:
#             print(plant[:-len(' - Flower')], file=plants)


# plants_filename = "flowers_write.txt"
# with open(file=plants_filename, mode='w') as plants:
#     for plant in data:
#         if 'Flower' in plant:
#             plants.write(plant[:-len(' - Flower')])


filename = "test_numbers.txt"
# with open(filename, "w") as test:
#     for i in range(10):
#         print(i, file=test)

with open(filename, "w") as test:
    for i in range(10):
        #        test.write(i)  # will error out as we can't .write non-text data to a
        #        non-text file
        test.write(str(i))
