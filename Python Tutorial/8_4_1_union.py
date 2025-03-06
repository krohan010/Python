# The union() method returns a new set with all items from both sets :

oddNumber = {1,3,5,7,9}
naturalNumber = {1,2,3,4,5,6}

# natural = naturalNumber.union(oddNumber)

# use pipe(|) operator instead of union() :
natural = naturalNumber | oddNumber

print(natural)

# Join Multiple sets :
realNumSet = {1, 1.5, -5, 56, 56.1}

# multiSet = naturalNumber.union(oddNumber, realNumSet)
multiSet = naturalNumber | oddNumber | realNumSet
print(multiSet)

# join list and tuples :
fruitList = ["Kiwi", "Orange"]
courseTuple = ("COPA", "DBSA", "ADCA")

allinone = oddNumber.union(naturalNumber, fruitList, courseTuple)
print(allinone)

# The  | operator only allows you to join sets with sets, and not with other data types
# like you can with the  union() method.


# The update() method inserts all items from one set into another set.
# It changes the original set and doesn't return a new set.

naturalNumber.update(oddNumber)
print(naturalNumber)


# Both union() and update() method excludes the duplicate items.
