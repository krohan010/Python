# Tuples are used to store multiple items in a single variable.
# Tuples item are Ordered & unchangeable and can be duplicate

# it is written with round brackets :
numTuple = (52, 58, 12, 46, 89, 97)
print(numTuple)
strTuple = ("Apple", "Banana", "Kiwi", "Mango")
print(strTuple)

# tuple items are indexed :
# numTuple[0] = 45                      # throw an error because tuples cannot modify or change
print(numTuple[0])

print(len(numTuple))                    # print length of the tuple

# create tuple with one item :
oneTuple = ("One")
print(type(oneTuple))                   # it will treat as a string

# Fix the problem :
anotheroneTuple = ("one",)
print(type(anotheroneTuple))            # print tuple class

#Constructor
anotherTuple = tuple(("One"))
print(anotherTuple)                         # output : ('O', 'n', 'e')
print(type(anotherTuple))

# A tuple can contains different types of data :
mixTuple = ("ABC", 98, "BCD", True, False, 112)
print(mixTuple)
print(type(mixTuple))