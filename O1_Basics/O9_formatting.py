for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2,
                                                                 i ** 3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2,
                                                                   i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))

# Pi is approximately 3.142857142857143
# Pi is approximately     3.142857
# Pi is approximately 3.14285714285714279370154144999105483293533325195312
# Pi is approximately 3.14285714285714279370154144999105483293533325195312
# Pi is approximately           3.14285714285714279370154144999105483293533325195312
# Pi is approximately 3.14285714285714279370154144999105483293533325195312
# Pi is approximately 3.142857142857142793701541449991054832935333251953125000

print()

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

print()

print(f"Pi is approx {22 / 7:12}")
print(f"Pi is approx {22 / 7:12f}")
print(f"Pi is approx {22 / 7:12.50f}")
print(f"Pi is approx {22 / 7:52.50f}")
print(f"Pi is approx {22 / 7:62.50f}")
print(f"Pi is approx {22 / 7:72.50f}")
print(f"Pi is approx {22 / 7:<72.50f}")
print(f"Pi is approx {22 / 7:<72.54f}")
print(f"Pi is approx {22 / 7:<72.59f}")

# Pi is approx 3.142857142857143
# Pi is approx     3.142857
# Pi is approx 3.14285714285714279370154144999105483293533325195312
# Pi is approx 3.14285714285714279370154144999105483293533325195312
# Pi is approx           3.14285714285714279370154144999105483293533325195312
# Pi is approx                     3.14285714285714279370154144999105483293533325195312
# Pi is approx 3.14285714285714279370154144999105483293533325195312
# Pi is approx 3.142857142857142793701541449991054832935333251953125000
# Pi is approx 3.14285714285714279370154144999105483293533325195312500000000
