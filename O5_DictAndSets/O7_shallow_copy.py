animals = {
    "lions": "scary",
    "elephants": "big",
    "teddy": "cuddly",
}

things = animals
animals["teddy"] = "toy"
print(things["teddy"])
# Output:   toy
print(animals["teddy"])
# Output:   toy

things = animals.copy()
animals["teddy"] = "toy"
print(things["teddy"])
# Output:   cuddly
print(animals["teddy"])
# Output:   toy

animals = {
    "lions": ["scary", "big", "cat"],
    "elephants": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

things = animals.copy()
print(things["teddy"])
print(animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
