def spam1():

    def spam2():

        def spam3():
            z = " even"
            z += y
            print(f"In spam3, locals are {locals()}")
            return z

        y = " more " + x
        y += spam3()
        print(f"In spam2, locals are {locals()}")
        return y

    x = "spam" + spam2()
    print(f"In spam1, locals are {locals()}")
    return x


print(spam1())
