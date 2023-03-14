import pickle

imelda = 'More Mayhem', 'Imelda May', '2011', (
    (1, 'Pulling the Rug'),
    (2, 'Psycho'),
    (3, 'Kentish Town Waltz'),
)

pickled_files = 'imelda.pickle'

# with open(pickled_files, 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)
#
# with open(pickled_files, 'rb') as imelda_pickled:
#     imd = pickle.load(imelda_pickled)
#
# print(type(imd))
# # Output:
# # <class 'tuple'>
#
# print(imd)
# # Output:
# # ('More Mayhem', 'Imelda May', '2011',
# # (
# #   (1, 'Pulling the Rug'),
# #   (2, 'Psycho'),
# #   (3, 'Kentish Town Waltz')
# #   ))


even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open(pickled_files, 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998392, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)

with open(pickled_files, 'rb') as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

print(imelda2)
album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)

for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)
print('=' * 40)

for i in even_list:
    print(i)
print(type(even_list))
print('=' * 40)

for i in odd_list:
    print(i)
print('=' * 40)

print(x)
print(type(x))
