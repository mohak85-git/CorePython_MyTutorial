vehicles = {"dream": "Honda 250T",
            'roadster': "BMR R1100",
            'er5': 'Kawasaki ER5',
            'can-am': 'Bombardier Can-Am 250',
            'virago': 'Yamaha XV250',
            'tenere': 'Yamaha XT650',
            'jimny': 'Suzuki Jimny 1.5',
            'fiesta': 'Ford Fiesta Ghia 1.4',
            }

# my_car = vehicles['fiesta']
# print(my_car)
#
# commuter = vehicles['virago']
# print(commuter)
#
# learner = vehicles.get('er5')
# print(learner)

for keys in vehicles:
    print(f"{keys}: {vehicles[keys]}")

# preferred method as it is faster
for key, value in vehicles.items():
    # .items() method is analogous to enumerate() function
    print(key, value, sep=': ')

# add new items to dictionary
vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"

# Update existing key with new value
vehicles['virago'] = 'Yamaha XV535'

# remove/delete dictionary entries
del vehicles['starfighter']

# del vehicles['f1']
# this will cause error as there is no 'f1' key in vehicles

# print(vehicles.pop('f1'))
# this will cause error as there is no 'f1' key in vehicles
print(vehicles.pop('f1', "You wish! Sell the Learjet and you might\
 afford a racing car."))
plane = vehicles.pop("learjet")
print(plane)

plane_again = vehicles.pop('learjet', "You've already pop'd the Learjet")
print(plane_again)
