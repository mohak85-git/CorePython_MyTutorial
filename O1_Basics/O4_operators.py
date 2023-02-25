a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0 => produces float result
print(a // b)   # 4 => called as floor division (aka integer division), rounds
#                 down towards minus infinity.
print(a % b)    # 0 => modulo operator

print()

for i in range(1, a//b):
    print(i)

# for i in range(1, a/b):  # Causes error as a/b produces a floating type value
#     print(i)

print(a ** b)  # exponent operator, a raised to the power b.
