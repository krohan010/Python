# Set is used to store multiple values into a single variable
# written with curly brackets
# set items are unordered, unchangeable, non-iterable and cannot contain duplicate values

mySet = {"Hello", "python", "set"}
print(mySet)

fruitSet = {"Apple", "Banana", "Apple"}         # it ignore duplicate values
print(fruitSet)

# mix datatype set :
mixSet = {"ABC", "ADF", 58, 1, True, False, 0}      # True = 1 & False = 0 So it ignores duplicate values
print(mixSet)

# Length of set :
print(f"The length of mixSet is {len(mixSet)}")

# Data type :
print(type(mixSet))

# set constructor :
numSet = set((1, 5, 98, 64, 7, 52))
print(numSet)