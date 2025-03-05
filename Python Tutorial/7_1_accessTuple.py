# Tuples items are index so we can access it by using its index number inside of square brackets :

fruitTuple = ("Orange", "Apple", "Strawberry", "Mango")
print(fruitTuple[2])                        # Output : Strawberry

# Negative indexing start (-1) from the end
print(fruitTuple[-2])                       # Output : Strawberry

# Ranges of Index : Accessing items by specifying from the stand and to the end
# Pattern for access : include(start):exclude(end)
print(fruitTuple[1:3])                      # Output : ('Apple', 'Mango')

# By leaving out the start value, the range will start at the first item :
print(fruitTuple[:3])                       # output : ('Orange', 'Apple', 'Strawberry')

# By leaving out the end value, the range will go on to the end of the tuple:
print(fruitTuple[1:])                       # Output : ('Apple', 'Strawberry', 'Mango')

# Negative range indexing :
print(fruitTuple[-3:-1])                               # Output : ('Apple', 'Strawberry')
