# equation = bytes((207, 128, 114, 194, 178))
equation = b'\xcf\x80r\xc2\xb2'  # bytes literal is an array of bytes
# There are 5 values, starting with the hexadecimal value CF.
# That's followed by 80 in hex.
# Then a letter r.
# Finally, we have the two hex values C2 and B2.

print(equation)
print(type(equation))
print(len(equation))

print('*' * 30)

for b in equation:
    print(b, end=', ')
print()
