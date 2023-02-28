from O3a_contents_b4_replacing_with_contents_quantities import pantry, recipes

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

    display_dict[str(index + 1)] = key

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-" * 25)
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == '0':
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("\tchecking ingredients ...")
        ingredients = recipes[selected_item]
        print(f"\t\t{ingredients}")

        #   Check if all ingredients required are available in the pantry.
        for food_item in ingredients:
            if food_item not in pantry:
                print(f"\t\t\tYou do not have a {food_item} to cook a "
                      f"{selected_item}")
            else:
                print(f"\t\t\t{food_item} OK")
#             if required_quantity <= quantity_in_pantry:
#                 print(f"\t\t\t{food_item} OK")
#             else:
#                 quantity_to_buy = required_quantity - quantity_in_pantry
#                 print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
#                 add_shopping_item(shopping_list, food_item, quantity_to_buy)
#
# # for things in sorted(shopping_list):
# for things in shopping_list.items():
#     print(things)
