d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# v = d.values()
# print(v)
# d[10] = "ten"
# print(v)

# d2 = {
#     7: "lucky seven",
#     10: "ten",
#     3: "this is the new three"
# }

# d.update(d2)
# for key, value in d.items():
#     print(key, value)

# print()

# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)

# keys = d.keys()
# print(keys)
# d[10] = "ten"
# print(keys)

# for item in d:
# for item in d.keys():
#     print(item)

# new_dict = dict.fromkeys(pantry_items)
# print(new_dict)
# output: {'chicken': None, 'spam': None, 'egg': None, 'bread': None,
# 'lemon': None}

# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)
# output: {'chicken': 0, 'spam': 0, 'egg': 0, 'bread': 0, 'lemon': 0}

print(d.items())
