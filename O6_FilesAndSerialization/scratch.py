input_filename = "country_info.txt"

with open(input_filename) as country_file:
    header = country_file.readline()  # spare readline() to skip the header
    # for row in country_file:
    #     data = row.strip().split('|')
    print(header.rstrip().split('|'))
