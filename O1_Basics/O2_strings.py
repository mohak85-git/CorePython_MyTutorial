# You can use a pair of either single quote or double quote to define strings; you cannot use a mix of them.
# Unlike other programming languages, there is no difference between single quote and double quote literals.
# Other ways to include quotes as part of string literal are:
#       1.  Use escape character or
#       2.  Docstring.

print("Today is a good day to learn Python")
print('Python is fun')

print("Python's string are easy to use")
print('We can even include "quotes" in strings')
# If you need to include single quote inside a string, then use double quotes to define the string, vice versa.

print("hello" + "world")
# String Concatenation using + operator
# Note that there is no separator (space) between the two values in the output.

greeting = "Hello"
# name = "Bruce"
name = input("Please enter your name ")  # get input from user

print(greeting + ' ' + name)

age = 24
print(age)

# type() function returns the datatype of the object that is passed as an argument.
print(type(greeting))
print(type(age))

age = "2 years"
print(age)
print(type(age))
