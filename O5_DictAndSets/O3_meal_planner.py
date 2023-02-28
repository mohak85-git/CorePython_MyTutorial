from O3a_contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    # def add_shopping_item(data: list, item: str, amount: int) -> None:
    """Add a tuple containing 'item' and 'amount' to the 'data' dict."""
    # """Add a tuple containing 'item' and 'amount' to the 'data' list."""
    # data.append((item, amount))
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount

    data[item] = data.setdefault(item, 0) + amount


# We have to first transform the data in recipe dictionary into a menu type
# display.

# Below is short, efficient and pythonic way which makes use of dictionary
# comprehensions.
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

# Below is the long, non-pythonic and inefficient form
display_dict = {}
for index, key in enumerate(recipes):
    # print(index+1, key)
    # output:
    #     1 Butter chicken
    #     2 Chicken and chips
    #     3 Pizza
    #     4 Egg sandwich
    #     5 Beans on toast
    #     6 Spam a la tin

    display_dict[str(index+1)] = key

# recipes is a dictionary which contains sub-dictionaries (names of various
# dishes). The name of dish which is a key is a string and value is a list
# (of ingredients).
#   1.  Enumeration on recipes dictionary generates indexes for names of various
#   dishes. Using these indexes, create a new dictionary (display_dict) where
#   these indexes become the keys and the names of various dishes become the
#   values in display_dict dictionary.

shopping_list = {}
# shopping_list = []

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-"*25)
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

#   2.  Using the choice as key, retrieve the name of the desired dish from
#   display_dict dictionary. The name of dish becomes a key to retrieve the
#   ingredients from the sub-dictionary inside recipe dictionary.
    if choice == '0':
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("\tchecking ingredients ...")
        ingredients = recipes[selected_item]
        print(f"\t\t{ingredients}")

#   Check if all ingredients required are available in the pantry.
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            # if food_item not in pantry:
            #     print(f"\t\t\tYou do not have a {food_item} to cook a \
            #     {selected_item}")
            # else:
            #     print(f"\t\t\t{food_item} OK")
            if required_quantity <= quantity_in_pantry:
                print(f"\t\t\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

# for things in sorted(shopping_list):
for things in shopping_list.items():
    print(things)
