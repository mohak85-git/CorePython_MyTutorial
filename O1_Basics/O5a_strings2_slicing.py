#    ->             1
#         01234567890123
parrot = "Norwegian Blue"
#    <-  -    1
#        -43210987654321

print(parrot[0:6])      # Norweg
print(parrot[3:5])      # we
print(parrot[0:9])      # Norwegian
print(parrot[:9])       # Norwegian

print(parrot[10:14])    # Blue
print(parrot[10:])      # Blue

print(parrot[:6])       # Norweg
print(parrot[6:])       # ian Blue

print(parrot[:6] + parrot[6:])  # Norwegian Blue

print(parrot[:])        # Norwegian Blue
