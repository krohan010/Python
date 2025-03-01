# In this section we discuss about the most important methods of list :

# 1) APPEND() : Adds an element at the end of the list
numList = [5, 10, 15, 20, 25, 25]
numList.append(30)
print(numList)

# 2) CLEAR() : Removes all the elements from the list
randList = [1, 8, 6, 73, 91, 51]
print(randList)
randList.clear()
print(randList)

# 3) COPY() : Returns a copy of the list
numList2 = numList.copy()
print(numList2)

# 4) COUNT() : Returns the number of time an element appear in the list
print(f"The total number of times an element is appear in th list : {numList.count(25)}")

# 5) EXTEND() : Add the elements of a list (or any iterable), to the end of the current list
strList = ["ABC", "XYZ", "FGH"]
numList.extend(strList)
print(numList)

# 6) INDEX() : 	Returns the index of the first element with the specified value
print(f"The index number of FGH in the list is : {strList.index('FGH')}")

# 7) INSERT() : Adds an element at the specified position
strList.insert(1, "JKL")
print(strList)

# 8) POP() : Removes the element at the specified position
strList.pop(2)
print(strList)

# 9) REMOVE() : Removes the item with the specified value
strList.remove("ABC")
print(strList)

# 10) REVERSE() : Reverses the order of the list
strList.reverse()
print(strList)

# 11) SORT() : Sorts the list
numList3 = [400, 57, 79, 800, 46, 500, 185]
numList3.sort()
print(numList3)