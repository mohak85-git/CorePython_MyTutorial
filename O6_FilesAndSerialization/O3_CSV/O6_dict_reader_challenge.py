import csv

input_filename = "country_info.txt"

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    dict_data = csv.DictReader(country_file, delimiter='|')
    for row in dict_data:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row

print(countries)

while True:
    which_country = input("Enter the name of a country: ").casefold()
    if which_country in countries:
        print(f"The capital of {which_country} is {countries[which_country]['Capital']}")
    elif which_country == "quit":
        break
