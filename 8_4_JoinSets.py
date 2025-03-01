# There are various ways to join multiple set

oddNumSet = {1, 3, 5, 7, 9}
evenNumSet = {2, 4, 6, 8, 10}
realNumSet = {1, 1.5, -5, 56, 56.1}
naturalNumSet = {1, 2, 3, 4, 5}

# 1) update() method : Joins two more sets
# oddNumSet.update(evenNumSet, realNumSet)                  # store other set values into oddNumSet
# print(oddNumSet)

# 2) union() method : Joins two more sets & it can join other data type also like list, tuple
# realNumSet = oddNumSet.union(evenNumSet, naturalNumSet)         # here we need to store join list into a single set
# print(realNumSet)

# Other data type :
# list1 = ["A", "B", "C", "D"]
# tuple1 = ("a", "b", "c", "d")
# combineSet = naturalNumSet.union(tuple1, list1)                 # joins tuple, list & set
# print(combineSet)

# pipe (|) operator also join one or more than one set into in it.
# naturalNumSet =  oddNumSet | evenNumSet
# print(naturalNumSet)

# Intersection() method : keeps only the duplicate values from one or more than one set:
# commonSet = naturalNumSet.intersection(oddNumSet)                         # it stores the value into another set
# print(commonSet)

# intersection_update() method :
# oddNumSet.intersection_update(naturalNumSet)
# print(oddNumSet)                                                            # it updates the value and store in it.

# intersection with another data type such as tuple :
# randTuple = (1, 5, 4, 7)
# commonOfSet_Tuple = oddNumSet.intersection(randTuple)                       # Difference b/w sets and tuples
# print(commonOfSet_Tuple)


# we can also use & operator instead of intersection method :
# it cannot apply in other data type such as tuple, list
# commonSet = naturalNumSet & oddNumSet
# print(commonSet)                                # same output as intersection

# Difference : The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# it can use in different data types also such as tuples and lists
# evenNumSet = naturalNumSet.difference(oddNumSet)
# print(evenNumSet)

# use the (-) operator instead of the difference() method
# it cannot use in different data types
# evenNumSet = naturalNumSet - oddNumSet
# print(evenNumSet)                                   #same output as difference() method


