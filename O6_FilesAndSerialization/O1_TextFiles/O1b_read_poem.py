with open('Jabberwocky.txt', mode='r') as jabber:
    text = jabber.read()

print(text)
print(type(text))

# print the file with all characters in reverse order
for character in reversed(text):
    print(character, end='')
