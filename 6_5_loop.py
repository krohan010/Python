# We will learn how to print list items using for loop :

fruitList = ["Apple", "Banana", "Orange", "Graphs", "Kiwi"]

# For loop :
# for x in fruitList:
#     print(x)

# Shorthand for printing list elements
# [print(x) for x in fruitList]

# Print all elements using range method in for loop :
# range syntax : range(start, end, step)
print(range(5))                             #default : start = 0 & step = 1
for i in range(len(fruitList)):
    print(fruitList[i])

# While Loop :
i = 0                               # Initialization
# while i<len(fruitList):             # Condition
#     print(fruitList[i])
#     i = i + 1                       # Incrementation

