def banner_text(text=" ", screen_width=80):
    """_summary_

    Args:
        text (str, optional): _description_. Defaults to " ".
        screen_width (int, optional): _description_. Defaults to 80.
    """
#    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
    
    if text == '*':
        print("*" * screen_width)
    else:
        output_string = f"**{text.center(screen_width - 4)}**"
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
# banner_text(" ")
# banner_text(screen_width=66)
banner_text()
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")


# print(input.__doc__)
# print("*" * 80)
# print(banner_text.__doc__)
# print("*" * 80)
# help(input)
# print("*" * 80)
# help(banner_text)
