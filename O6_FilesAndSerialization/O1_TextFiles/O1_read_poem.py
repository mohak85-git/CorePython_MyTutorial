jabber = open(file='Jabberwocky.txt', mode='r')  # make use of absolute path
# jabber = open(file=r"E:\MyTutorial_CorePython\O6_TextFiles\Jabberwocky.txt",
#               mode='r')
#       Here, absolute path of the file is used.

# This is not a good way to open files; use the with operator.

print(jabber)

for line in jabber:
    # print(line, end='')
    # OR
    print(line.strip())  # .strip() method removes whitespace chars (space, tab
    # and newline) from both ends of a line.
    # .rstrip() and .lstrip() are also available.

jabber.close()
