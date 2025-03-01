# This section describes about the sorting of an list :

fruitList = ["Strawberry", "Pine-Apple", "Kiwi", "Mango"]
numList = [14, 100, 54, 78, 12, 98, 12, 46]
print(fruitList)

# Sort() method is used to sort an items in ascending order by default :
fruitList.sort()
print(fruitList)

print(numList)
# Sort Numbers by default smaller to larger
numList.sort()
print(numList)

# Sort Alphabets Descending order
fruitList.sort(reverse=True)
print(fruitList)

# Sort Numbers Larger to smaller :
numList.sort(reverse=True)
print(numList)

# Customize Sort Function :
# Sort numbers which is closest to the 50
def myfunc(n):
    return abs(n - 50)
numList.sort(key=myfunc)
print(numList)

# Sort() method is case sensitive, resulting in all capital letter being sorted before lower case

alphaList = ["W", "r", "R", "D", "f", "G", 'o']
print(alphaList)
alphaList.sort()                        # sort first capital letter then small letter.
print(alphaList)

# Case Insensitive sort :
alphaList.sort(key = str.lower)
print(alphaList)

# reverse() method sort the current list in reverse order :
alphaList.reverse()
print(alphaList)
