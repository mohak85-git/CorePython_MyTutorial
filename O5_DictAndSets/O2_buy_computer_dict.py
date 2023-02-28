available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive"
                   }

current_choice = None
computer_parts = {}   # empty dictionary

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            # it's already in, so remove it
            print(f"Removing {current_choice}")
            del computer_parts[current_choice]
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains: {computer_parts}")
    else:
        print("Available parts are:")
        for key, part in available_parts.items():
            print(f"\t{key}: {part}")
        print("0: to finish")

    current_choice = input("> ")
