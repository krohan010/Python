
fruitStr = "Apple, Banana, Mango, Orange"

fruitList = fruitStr.split(",")
print(fruitList)

for i in range(len(fruitList)):
    fruitList[i] = fruitList[i].strip()

print(fruitList)
fruitList.append("Apple")

if "Mango" in fruitList:
    print("Founded")
else:
    print("Not Founded")

if fruitList.count("Apple"):
    fruitList.remove("Apple")
    print("Deleted")
else:
    print("Not Deleted")
print(fruitList)

for i in range(0, 10):
    print(i)

# Unpacking
x1, x2, *x3 = fruitList
print(x3)