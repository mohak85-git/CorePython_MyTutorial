# Difference
#
# For this exercise, imagine you're working on a retail web site.
#
# Customers can favourite certain items that they're interested in.
#
# They can also purchase items, by adding them to their shopping basket – or cart.
#
# As they browse the various items for sale, the web page will display a list
# of items that they might be interested in purchasing. That list will be the
# items they've marked as "favourites'.
#
# But we don't want to suggest items that the customer has already added to
# their shopping basket.
#
# The code to create the favourites and basket sets has already been written
# and tested.
#
# Your task is to create a sorted list of the customer's favourite items,
# without any items that are in their basket.
#
# Develop the code in your IDE, before running it in here.
#
# You must call your list suggestions. That's the name that the on-line code
# checker will be looking for.
#
# Also, don't change the names of the two sets that we've created for you.

favourites = {'door screen',
              'frying pan',
              'roller blind',
              'football',
              'coffee grinder',
              'bush hat',
              'stirling engine',
              'cachemira cd',
              'shirt',
              }

basket = {'garlic crusher',
          'stirling engine',
          'frying pan',
          'shirt',
          'bush hat',
          }

# Add your code here.
suggestions = sorted(favourites.difference(basket))
print(suggestions)
