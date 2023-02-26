# Variable number of arguments

# Write a function to calculate the sum of all numbers passed as its arguments.

# Your function should be called sum_numbers and should define a single variable
# argument (i.e. a star argument) that will get the values to sum.

# To pass in this on-line interpreter, your function must contain a Docstring.

# The parameters and return value must be annotated. Be careful here, you may 
# want to review the lecture Function annotations and type hints, or check 
# PEP 484 to see what it says about annotating numerical arguments and return 
# types.

# Test the function with the following values:
#     Values              Result
#     1, 2, 3             6
#     8, 20, 2            30
#     12.5, 3.147, 98.1   113.747
#     1.1, 2.2, 5.5       8.8

# Those are just example data, this system will check your function with random 
# sequences of values.

def sum_numbers(*args: float) -> float:
    """_summary_

    Returns:
        float: _description_
    """
    total = 0
    for arg in args:
        total += arg

    return total


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
