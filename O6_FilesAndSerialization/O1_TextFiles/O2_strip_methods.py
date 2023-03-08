filename = 'Jabberwocky.txt'
with open(filename) as poem:
    firstline = poem.readline().rstrip()  # read only 1st line

print(firstline)
print('-' * 45)

chars = "'"
no_apostrophe = firstline.strip(chars)
print(no_apostrophe)
print('-' * 45)

chars = "'Twas"
no_apostrophe = firstline.strip(chars)
print(no_apostrophe)
print('-' * 45)

chars = "'Twasebv"
no_apostrophe = firstline.strip(chars)
print(no_apostrophe)
print('-' * 45)
