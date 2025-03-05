# python sets are unordered it means that you cannot access set item by referring to an index or key.

fruitSet = {"Apple", "Mango", "Banana", "Strawberry"}

# Access items using for loop :
for item in fruitSet:
    print(item)

# To check whether a value exist in set or not
print("Apple" in fruitSet)                  # True
print("Mango" not in fruitSet)              # False
