with open(file='Jabberwocky.txt', mode='r') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print("*" * 80)

# .readline() is least used as the same result can be achieved by just iterating
# over the file object itself.

with open(file="Jabberwocky.txt") as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break
