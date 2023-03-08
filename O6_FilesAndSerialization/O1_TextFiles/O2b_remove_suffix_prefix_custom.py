def remove_prefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]


def remove_suffix(string: str, suffix: str) -> str:
    if string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]


filename = 'Jabberwocky.txt'
with open(filename) as poem:
    firstline = poem.readline().rstrip()  # read only 1st line

twas_removed = firstline.removeprefix("'Twas")
print(twas_removed)

toves_removed = firstline.removesuffix("toves")
print(toves_removed)

print('-' * 45)

twas_removed = remove_prefix(string=firstline, prefix="'Twas")
print(twas_removed)

toves_removed = remove_suffix(string=firstline, suffix="toves")
print(toves_removed)
