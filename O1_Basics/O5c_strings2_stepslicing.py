#    ->             1
#         01234567890123
parrot = "Norwegian Blue"
#    <-  -    1
#        -43210987654321

print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

number = "9,223:372;036 854,775;807"
# print(number[1::4])     # ,:; ,;
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else ' ' for char in number) \
    .split()

print(values)   # ['9', '223', '372', '036', '854', '775', '807']
print([int(val) for val in values])  # [9, 223, 372, 36, 854, 775, 807]
