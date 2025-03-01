# When we create a tuple , we normally assign values to it. This is called packing
fruitTuple = ("Orange", "Apple", "Strawberry", "Mango")

# Extract the values back into the variable. this is called unpacking :
# Syntax -> Variable Names = tuple name
# fruit1, fruit2, fruit3, fruit4 = fruitTuple
# print(fruit1)
# print(fruit2)
# print(fruit3)
# print(fruit4)

# The number of variables must match the number of values in the tuple,
# if not, you must use an asterisk to collect the remaining values as a list.
# fruit1, *fruit2 = fruitTuple
# print(fruit1)                           # String : Orange
# print(fruit2)                           # List : ['Apple', 'Strawberry', 'Mango']


# If Asterisk symbol added at the starting variable then :
*fruit1, fruit2 = fruitTuple
print(fruit1)                               # List : ['Orange', 'Apple', 'Strawberry']
print(fruit2)                               # Strig : Mango