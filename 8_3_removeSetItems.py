# Remove the items from the set :

# First way : remove() method -> if an item does not exist , it throws an error :
fruitSet = {"Apple", "Mango", "Banana", "Strawberry"}
#fruitSet.remove("Kiwi")                         # throws an error because kiwi not exist in the set
# fruitSet.remove("Banana")
# print(fruitSet)

# Second way : discard() method -> if an specified item does not exist then it does not throw an error
# fruitSet.discard("Kiwi")                        # doesn't throw an error
# fruitSet.discard("Apple")
# print(fruitSet)

# Third way : pop() Method -> sets are unordered so that it deletes one random item from the set
# fruitSet.pop()                                      # doesn't know the deleted item
delItem = fruitSet.pop()                              # Deleted item stored in it.
print(F"Deleted item is : {delItem}")
print(F"Rest Set are : {fruitSet}")

# Clear() Method removes all items from the set but set exist :
# fruitSet.clear()
# print(fruitSet)

# del keyword totally deleted an set
del fruitSet
# print(fruitSet)                                 # Throw an error because it's not exist