input_filename = "country_info.txt"

countries = {}
with open(input_filename) as country_file:
    country_file.readline()  # spare readline() to skip the header
    for row in country_file:
        data = row.strip().split('|')
        # print(data)
        country, capital, code, code3, dialing, timezone, currency = data
        # List unpacking
        # print(country, capital, code, code3, dialing, timezone, currency,
        #       sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict

print(countries)
while True:
    which_country = input("Enter the name of a country: ").casefold()
    if which_country in countries:
        print(f"The capital of {which_country} is "
              f"{countries[which_country]['capital']}")
    elif which_country == "quit":
        break
