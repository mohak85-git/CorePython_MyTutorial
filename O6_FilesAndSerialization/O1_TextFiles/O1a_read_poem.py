with open(file='Jabberwocky.txt', mode='r') as jabber:
    # for line in jabber:
    #     print(line.rstrip())
    lines = jabber.readlines()  # reads the entire file as a single list of
    # strings where each line is an item of the list

print(type(lines))
print(lines)    # prints the list

print(lines[-1:])   # prints the last item of the list/ last line

for line in reversed(lines):    # iterates over the list in reverse order
    print(line, end='')     # prints the list in reverse order
