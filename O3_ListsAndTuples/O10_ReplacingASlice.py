computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

computer_parts[3:] = "trackball"  # This is wrong
print(computer_parts[3:])
print(computer_parts)

computer_parts[3:] = ["trackball"]
print(computer_parts)
