letters = "abcdefghijklmnopqrstuvwxyz"
#          01234567890123456789012345
#                    1         2

backwards = letters[25:0:-1]
print(backwards)        # zyxwvutsrqponmlkjihgfedcb (upto but not including)

backwards = letters[::-1]
print(backwards)        # zyxwvutsrqponmlkjihgfedcba

print(letters[16:13:-1])    # qpo

print(letters[4::-1])       # edcba

print(letters[25:17:-1])    # zyxwvuts
print(letters[:-9:-1])      # zyxwvuts

print(letters[-4:])     # wxyz
print(letters[-1:])     # z
print(letters[:1])      # a , returns empty string if the base string is an
#                         empty string
print(letters[0])       # a , causes error if the string is empty

print(letters[25::-2])  # zxvtrpnljhfdb
