animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           "Swallow",
           "Hedgehog",
           "Wren",
           'Aardvark',
           'Cat',
           }

birds = {'Robin', 'Swallow', 'Wren'}

print(f'birds is a subset of animals: {birds.issubset(animals)}')
print(f'animals is a superset of birds: {animals.issuperset(birds)}')

print(f'birds is superset of animals: {birds.issuperset(animals)}')

print(birds <= animals)  # subset
print(birds < animals)  # proper subset

print('*' * 80)

garden_birds = {'Swallow', 'Wren', 'Robin'}
print(garden_birds == birds)  # are sets equal? Yes
print(garden_birds <= birds)  # garden_birds a subset of birds? Yes
print(garden_birds < birds)  # garden_birds a proper subset of birds? No

print('*' * 80)

more_birds = {'Wren', 'Budgie', 'Swallow'}
print(garden_birds >= more_birds)  # garden_birds a superset of more_birds? No
