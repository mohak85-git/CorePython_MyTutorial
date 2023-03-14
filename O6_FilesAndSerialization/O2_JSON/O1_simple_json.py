import json

# languages = [  # list of tuples
#     ('ABC', 1987),
#     ('Algol 68', 1968),
#     ('APL', 1962),
#     ('C', 1973),
#     ('Haskell', 1990),
#     ('Lisp', 1958),
#     ('Modula-2', 1977),
#     ('Perl', 1987),
# ]

languages = [  # list of lists
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

# with open(file='test.json', mode='w', encoding='utf-8') as testfile:
#     json.dump(languages, testfile)

with open(file='test.json', mode='r', encoding='utf-8') as testfile:
    data = json.load(testfile)

print(data)
print(data[2])
