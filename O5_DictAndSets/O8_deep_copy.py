import copy

animals = {
    "lions": ["scary", "big", "cat"],
    "elephants": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

things = copy.deepcopy(animals)  # Performs deep copy
print(things["teddy"])
print(animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
