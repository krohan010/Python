# The Difference between the sort and sorted method in python :

# Sort() method :
# This is a method that is used specifically with lists(case sensitive).
# It modifies the original list in-place. This means that after you call sort(), the original list's order is changed.

fruitList = ["Orange", "Kiwi", "Apple", "Strawberry"]
print(fruitList.sort())             # return Nothing
fruitList.sort()                    # sort list in-place
print(fruitList)


# Sorted() function:
# This is built-in function that can be used with any iterable (list, tuples & strings).
# it returns a new sorted list. the original iterable remains unchanged.
# It returns the new sorted list

randTuple = [142, 25, 8, 97, 46, 25]
print(sorted(randTuple))                # it returns sorted tuple

anotherList = sorted(fruitList)
print(anotherList)
