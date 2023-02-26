
# string    format specifier = s
# int       format specifier = d
# float     format specifier = f
# hex       format specifier = x
# octal     format specifier = o
# binary    format specifier does not exist for Python 2. Convert integer
#           to string representation of binary number.

from math import pi

print("%" * 20, " ^ center specifier on cubed")

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2,
                                                                   i ** 3))

print()
print("%" * 20, " format() method")
print()

# With no type specifiers, float will show min 1 decimal place
print(f"Pi is approximately {22 / 7:12}")

# With the type specifier, float defaults to 6 decimal places
print(f"Pi is approximately {22 / 7:12f}")

# With Leading Zeros
print(f"Pi is approximately {22 / 7:012f}")

# Decimal places takes precedence over width.
print(f"Pi is approximately {22 / 7:12.50f}")

# 50 decimal places results in 52 characters with this value
print(f"Pi is approximately {22 / 7:52.50f}")

# Width of 62 is 10 characters more than this value
print(f"Pi is approximately {22 / 7:62.50f}")

# Width is now 20 more than this value, but left aligned
print(f"Pi is approximately {22 / 7:<72.50f}")

# Add another 4: also left aligned
print(f"Pi is approximately {22 / 7:<72.54f}")

# The number of decimal places is now at a realistic accuracy for approximating
# PI.
print(f"Pi is approximately {22 / 7:12.2f}")

# Use math.pi if you really want to use the value of pi.
print(f"From the math module: math.pi is approximately {pi:>15.8f}")
