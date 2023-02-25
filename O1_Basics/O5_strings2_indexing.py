#    ->             1
#         01234567890123
parrot = "Norwegian Blue"
#    <-  -    1
#        -43210987654321

print(parrot)

# print "we win", using +ve index
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

# print "we win", using -ve index
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

# Negative index = Positive index - Length of string
print(f"Length of the string is: {len(parrot)}")
print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])
