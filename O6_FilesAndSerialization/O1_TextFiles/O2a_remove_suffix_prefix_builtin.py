filename = 'Jabberwocky.txt'
with open(filename) as poem:
    firstline = poem.readline().rstrip()  # read only 1st line

twas_removed = firstline.removeprefix("'Twas")
print(twas_removed)

toves_removed = firstline.removesuffix("toves")
print(toves_removed)
