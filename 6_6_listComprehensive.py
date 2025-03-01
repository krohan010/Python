fruitList = ["Apple", "Banana", "Orange", "Ananas"]
# newList = []

# for x in fruitList:
#     if "A" in x:
#         newList.append(x)
#
# print(newList)

# Now, same output but using comprehensive way :
newList = [x for x in fruitList if "A" in x]
print(newList)

animals = ["lion", "tiger", "monkey", "elephant", "frog"]
# filter_animal = [animal for animal in range(len(animals))]
# print(filter_animal)

# store Animals name in Capital format
cap_animals = [animal.upper() for animal in animals]
print(cap_animals)

# return "Kiwi" instead of Banana :
newFruitList = [fruit if fruit != "Banana" else "Kiwi" for fruit in fruitList]
print(newFruitList)