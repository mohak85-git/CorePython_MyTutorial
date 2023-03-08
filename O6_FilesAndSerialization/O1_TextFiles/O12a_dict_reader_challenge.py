import csv

input_filename = "country_info.txt"

dialect = csv.excel
dialect.delimiter = '|'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    # Get the column headings from the first line of the file
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()

    dict_data = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in dict_data:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row

print(countries)

while True:
    which_country = input("Enter the name of a country: ").casefold()
    if which_country in countries:
        print(f"The capital of {which_country} is {countries[which_country]['capital']}")
    elif which_country.casefold() == "quit":
        break
