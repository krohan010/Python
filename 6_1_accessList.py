# This section explains about  How to access list items and elements :

fruitList = ["Apple", "Banana", "Orange", "Kiwi", "WaterMelon"]
# in python list is indexed from 0 to ...
print(fruitList[1])                         # return second item of list

print(fruitList[-1])                        # negative indexing counts at the end

# Range of Index :
# syntax -> fruitList[start : end]
# start value must be included but not the end value
print(fruitList[1:3])

print(fruitList[-4 : -1])                   # Negative value counts indexing from the end

# Leaving blank at start -> counts from the starting.
# Leaving blank at end  -> counts to the end of the list.

print(fruitList[2 : ])                      # the range include from the 2 to end

print(fruitList[ : 4])                      #the rang included from the starting to the 4 index of list

print(fruitList[-4 : ])                     # the range lies from the -4 to the end of the list

print(fruitList[ : -2])                     # the range lies from the starting to the -2 end