def test_star(*args):
    print(args)
    for x in args:
        print(x)


print("\n" * 2)
test_star(0, 1, 2, 3, 4, 5)
test_star()

print("\n" * 3)


def average(*args):
    print(type(args))
    print(f"args is {args}")
    print("*args is ", *args)
    mean = 0
    for arg in args:
        mean += arg

    return mean/len(args)


print(average(1, 2, 3, 4))
