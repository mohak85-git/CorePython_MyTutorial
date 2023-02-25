a = b = c = d = 12
print(c)

x, y, z = 1, 2, 3  # tuple literal unpacking
print(x)
print(y)
print(z) 

print(type(x))
print(type(y))
print(type(z))

print('\n' * 2)

data = 1, 2, 76  # data represents tuple

x, y, z = data  # tuple unpacking
print(x)
print(y)
print(z)

for index, char in enumerate("abcdefgh"):  # enumarete() returns a tuple
    print(index, char)

for t in enumerate("abcdefgh"):  # enumarete() returns a tuple
    print(t)
    index, char = t
    print(index, char)

date_list = [1, 2, 76]
p, q, r = date_list  # lists can also be unpacked
print(p, q, r)

print(*date_list)  # another way of unpacking lists
print(*data)  # another way of unpacking tuples

table = ("Coffee Table", 200, 100, 75, 34.50)
name, length, width, height, price = table
print(length * width)

