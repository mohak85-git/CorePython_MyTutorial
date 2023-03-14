# imelda = "More Mayhem", "Imelda May", "2013", (
#     (1, "Pulling the Rug"),
#     (2, "Psycho"),
#     (3, "Kentish Town Waltz")
# )

# with open(file="imelda.txt", mode='wt') as imelda_file:
#     print(type(imelda))
#     print(imelda, file=imelda_file)

with open(file="imelda.txt", mode='rt') as imelda_file:
    contents = imelda_file.readline()

    print(type(contents))
    print(contents)

    imelda = eval(contents)
    print(type(imelda))
    print(imelda)

title, artist, year, track = imelda
print(title)
print(artist)
print(year)
print(track)
