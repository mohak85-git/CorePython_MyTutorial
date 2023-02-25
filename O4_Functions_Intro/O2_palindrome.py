def is_palindrome(string: str) -> bool:
    # backwards = string[::-1]
    # return backwards == string    
    return string.casefold() == string[::-1].casefold()


def palindrome_sentence(sentence: str) -> bool:
    string = ''
    for char in sentence:
        if char.isalnum():
            string += char
    # return string.casefold() == string[::-1].casefold()
    return is_palindrome(string)


# word = input("Please enter a word to check: ")
# Example: malayalam; Racecar
# if is_palindrome(word):
#     print(f"'{word}' is a palindrome.")
# else:
#     print(f"'{word}' is a not palindrome.")


sentence = input("Please enter a sentence to check: ")
# Example: Was it a car or a cat i saw; do geese see god
if palindrome_sentence(sentence):
    print(f"'{sentence}' is a palindrome.")
else:
    print(f"'{sentence}' is a not palindrome.")
