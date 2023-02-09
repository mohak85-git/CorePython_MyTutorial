letters = "abcdefghijklmnopqrstuvwxyz"
#          01234567890123456789012345
#                    1         2

backwards = letters[25:0:-1]
print(backwards)        # zyxwvutsrqponmlkjihgfedcb


backwards = letters[::-1]
print(backwards)        # zyxwvutsrqponmlkjihgfedcba

print(letters[16:13:-1])    # qpo

print(letters[4::-1])       # edcba

print(letters[25:17:-1])    # zyxwvuts
print(letters[:-9:-1])      # zyxwvuts

print(letters[-4:])     # wxyz
print(letters[-1:])     # z
print(letters[:1])      # a
print(letters[0])       # a


print(letters[25::-2])
