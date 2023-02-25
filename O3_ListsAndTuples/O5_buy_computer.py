available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"
                   ]

valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
# print(valid_choices)

current_choice = "_"
computer_parts = []  # create an empty list

while current_choice != '0':

    if current_choice in valid_choices:

        # print(f"Adding {current_choice}.")
        index = int(current_choice) - 1
        chosen_part = available_parts[index]

        if chosen_part in computer_parts:
            print(f"Removing {chosen_part} from the list.")
            computer_parts.remove(chosen_part)  # remove the chosen part
        else:
            computer_parts.append(chosen_part)
            print(f"Adding {chosen_part} to the list.")

        print(f"Your list now contains:{computer_parts}")

    # if current_choice in "12345":
    #     print(f'Adding {current_choice}')
    #     if current_choice == "1":
    #         computer_parts.append("computer")
    #     elif current_choice == '2':
    #         computer_parts.append("monitor")
    #     elif current_choice == '3':
    #         computer_parts.append("keyboard")
    #     elif current_choice == '4':
    #         computer_parts.append("mouse")
    #     elif current_choice == '5':
    #         computer_parts.append("mouse mat")
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print(f"\t{number + 1}:\t{part}")
        # for parts in available_parts:
        #     print(f"\t{available_parts.index(parts) + 1}:\t{parts}")
        print("\n\tOR enter 0 to finish.")

    current_choice = input()
# if computer_parts == []:
# if not any(computer_parts):
if not computer_parts:
    print("You have not added any computer parts")
else:
    print(computer_parts)
