import os

# working_directory = "F:\\Kurulus Osman"
listing = os.walk(working_directory)
base_name = "Kurulus Osman"
season_number = 0
for root, directory, files in os.walk(working_directory):
    if files:
        season_number += 1
        print(f"Current directory is: {root}")
        for file in files:
            split_filename = file.split('.')
            file_number = split_filename[0]
            file_extn = split_filename[2]
            new_filename = file_number + '-' + base_name + f" S{season_number}-E" + file_number + '.' + file_extn
            src = f"{root}\\{file}"
            dst = f"{root}\\{new_filename}"

            os.rename(src=src, dst=dst)
