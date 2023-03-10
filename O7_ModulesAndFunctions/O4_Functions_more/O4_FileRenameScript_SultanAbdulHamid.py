import os

# working_directory = "F:\\Sultan Abdul Hamid\\Season 1"
listing = os.walk(working_directory)
base_name = "Payitaht Sultan Abdul Hamid S1-E"

for filename in os.listdir(working_directory):
    split_filename = filename.split('.')
    file_number = split_filename[0]
    file_extn = split_filename[2]
    new_filename = file_number + '-' + base_name + file_number + '.' + file_extn
    src = f"{working_directory}\\{filename}"
    dst = f"{working_directory}\\{new_filename}"

    os.rename(src=src, dst=dst)
