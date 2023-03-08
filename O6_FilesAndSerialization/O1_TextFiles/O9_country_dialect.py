import csv

input_filename = 'country_info.txt'

# with open(file=input_filename, encoding='utf-8', newline='') as countries_data:
#     data = csv.reader(countries_data, delimiter='|')
#     for row in data:
#         print(row)

# with open(input_filename, encoding='utf-8', newline='') as countries_data:
#     sample = countries_data.read()
#     country_dialect = csv.Sniffer().sniff(sample)
#     countries_data.seek(0)
#     country_reader = csv.reader(countries_data, dialect=country_dialect)
#     for row in country_reader:
#         print(row)

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    countries_data.seek(0)
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    # for row in country_reader:
    #     print(row)

# print('*' * 80)

attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]

for attribute in attributes:
    # print(f"{attribute}: {getattr(country_dialect, attribute)}")
    print(f"{attribute}: {repr(getattr(country_dialect, attribute))}")
