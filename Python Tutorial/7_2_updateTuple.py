# Tuples are unchangeable and Immutable.
# It means that you cannot change its values, once it is created

# Then, how can we change its values?
#Solution ->
fruitTuple = ("Orange", "Apple", "Strawberry", "Mango")

#Replace "Kiwi" with "Orange"

#Step 1: convert tuple into list
fruitList = list(fruitTuple)

#step 2: Change list values
fruitList[0] = "Kiwi"

#step 3: Then convert list into same Tuple
fruitTuple = tuple(fruitList)
print(fruitTuple)

# Add items into tuple :
# Convert tuple into list
# Add items into list and
# then convert back into tuple

# Another way to add tuples into tuples :
oneFruitTuple = ("Papaya",)
fruitList += oneFruitTuple
print(fruitList)

# Delete items from tuple :
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

# Delete complete tuple
del fruitTuple
# print(fruitTuple)                     # throws an error because tuple no more exist.