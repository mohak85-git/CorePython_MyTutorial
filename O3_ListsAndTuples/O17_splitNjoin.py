numbers = "9,223,372,036,854,775,807"
print(numbers.split(','))

generated_list = ["9", " ",
                  "2", "2", "3", " ",
                  "3", "7", "2", " ",
                  "0", "3", "6", " ",
                  "8", "5", "4", " ",
                  "7", "7", "5", " ",
                  "8", "0", "7"]

values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)
