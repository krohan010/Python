# Intersection() method returns duplicate values.
# it means that returns item which present in both sets

oddNumber = {1,3,5,7,9}
naturalNumber = {1,2,3,4,5,6}

# either we can store items into variable or directly print the return items :

# commonSet = naturalNumber.intersection(oddNumber)
# print(commonSet)

print(oddNumber.intersection(naturalNumber))

# Return duplicate value using & operator :
commonSet = oddNumber & naturalNumber
print(commonSet)

favLangSet = {"Python", "JS", "Java"}
PopularLangTuple = ("C", "C++", "Python", "Java")
knownList = ["Python", "Java", "HTML", "JS"]

commonLang = favLangSet.intersection(PopularLangTuple, knownList)
print(commonLang)


# intersection_update() method will only keep the duplicate values.
# but it will change the original set instead of running a new set.

oddNumber.intersection_update(naturalNumber)
print(oddNumber)