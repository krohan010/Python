# Using loops for printing the tuple elements :
# Tuple is one of the iterative built-in data type
fruitTuple = ("Orange", "Apple", "Strawberry", "Mango")

# For loop
# for item in fruitTuple:
#     print(item)

#shorthand for "FOR" loop :
# [print(x) for x in fruitTuple]

# print all elements by using range method :
for i in range(len(fruitTuple)):
    print(f"Item {i} -> {fruitTuple[i]}")

# using while loop
i = 0
while(i < len(fruitTuple)):
    print(fruitTuple[i])
    i += 1