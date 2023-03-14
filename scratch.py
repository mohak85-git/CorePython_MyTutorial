# list1 = ['a', 'b', 'c', 'd', 'e']
# list2 = list1[:]
# list1[0] = '1'
# print(list2)


# for i in range(1, 18, 2):
#     print(('*' * i).center(18))
k = int(input("Please enter k: "))
x = int(input("Please enter x: "))

kdig = 10**(k-1)
print(kdig)

if kdig%x != 0:
    z1 = kdig // x
    print(z1)
    z2 = z1 * x
    print(z2)
    z3 = kdig - z2
    print(z3)
    z4 = x - z3
    print(z4)
    answer = kdig + z4
    print(f"answer is {answer}")
else:
    print(f'{kdig} is the smallest {k} digit number divisible by {x}')