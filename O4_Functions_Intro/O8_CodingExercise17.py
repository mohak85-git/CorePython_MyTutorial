# Fizz Buzz

# For this exercise, you'll write a function that returns the next answer, in 
# the game of fizz buzz.

# It's a simple game, usually played with 2 or more people.

# You start counting, in turn. That's easy enough, but there's a complication.

# If the number is divisible by 3, you say "fizz" instead.

# If it's divisible by 5, you say "buzz".

# And if it's divisible by both 3 and 5, you say "fizz buzz".

# The function must be called fizz_buzz

# Your fizz_buzz function should return the correct word ("fizz", "buzz" or 
# "fizz buzz"), or the number if it's not divisible by either 3 or 5.

# The function will always return a string. When you return the number, 
# therefore, you should convert it to a string first.

# Remember to annotate your function, and include a Docstring.


# Include a for loop, to test your function for values from 1 to 100, inclusive.

def fizz_buzz(n: int) -> str:
    """_summary_

    Args:
        n (int): _description_

    Returns:
        str: _description_
    """
    if n%3 == 0 and n%5 == 0:
        return "fizz buzz"
    elif n%3 == 0:
        return "fizz"
    elif n%5 == 0:
        return 'buzz'
    else:
        return str(n)


for i in range(1, 101):
    print(fizz_buzz(i))
