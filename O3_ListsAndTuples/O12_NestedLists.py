even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]  # [[2, 4, 6, 8], [1, 3, 5, 7, 9]]
print(numbers)

for number_lists in numbers:
    print(number_lists)

    for values in number_lists:
        print(values)
