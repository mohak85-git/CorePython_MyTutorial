# The Magical Adder
#
# For this exercise, you have to write a python program which prompts the user 
# to enter three integers separated by ",".
# The user input is of the form: a,b,c, where a, b and c are numbers.
# Your program should calculate and display the result of the calculation:
# a + b - c
#
# Examples:
# 1. > Please enter three numbers: 10,11,10
#    11
#
# 2. > Please enter three numbers: 7,5,-1
#    13 

# Take input from the user
user_input = input("Please enter three numbers: ")

# Split the given input string into 3 parts
string_tokens = user_input.split(",")

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# Calculate the result: a + b - c
a, b, c = int_tokens    # list unpacking
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
print(result)
