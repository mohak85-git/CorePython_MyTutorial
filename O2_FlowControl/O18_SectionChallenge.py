choice = '-'

# while True:
#     if choice == '0':
#         break
#     elif choice in "12345":
#         print(f"You chose {choice}")
#     else:
#         print("Please choose your option from the list below: ")
#         print("1.    Learn Python")
#         print("2.    Learn Java")
#         print("3.    Go swimming")
#         print("4.    Have dinner")
#         print("5.    Go to bed")
#         print("0.    Exit")

# while choice != '0':
#     if choice in "12345":
#         print(f"You chose {choice}")
#     else:
#         print("Please choose your option from the list below: ")
#         print("1.    Learn Python")
#         print("2.    Learn Java")
#         print("3.    Go swimming")
#         print("4.    Have dinner")
#         print("5.    Go to bed")
#         print("0.    Exit")
# 
#     choice = input()

#
# options = ["Exit", "Learn Python", "Learn Java", "Go swimming",
# "Have dinner", "Go to bed"]
#
# while choice != '0':
#     if choice in "12345":
#         print(f"You chose {choice}")
#     else:
#         print("Please choose your option from the list below: ")
#         for option in options:
#             print(f"{options.index(option)}.\t{option}")

# # index() function gives the position of element in sequence object
# # For larger objects, enumeration() is much more efficient than indexing.

#     choice = input()
#

options = ["Exit",
           "Learn Python",
           "Learn Java",
           "Go swimming",
           "Have dinner",
           "Go to bed"]

while choice != '0':
    if choice in "12345":
        print(f"You chose {choice}")
    else:
        print("Please choose your option from the list below: ")
        for index, option in enumerate(options):
            print(f"{index}.\t{option}")

    choice = input()
