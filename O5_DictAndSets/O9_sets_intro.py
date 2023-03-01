farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse', 'hen'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}
# Ordering is not important for sets to be equal
if more_animals == farm_animals:  # check for equality
    print("The sets are equal")
else:
    print("The sets are different")
