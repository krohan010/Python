# The difference method will return a new set that will contain only the items from the set that are not present in the current set

oddNumber = {1,3,5,7,9}
naturalNumber = {1,2,3,4,5,6}

# primeNumber = naturalNumber.difference(oddNumber)
restNumber = oddNumber.difference(naturalNumber)
print(restNumber)

# use - operator instead of difference method :
primeNumber = naturalNumber - oddNumber
print(primeNumber)

# The - operator only allows you to join sets with sets, and not with other data types
# like you can with the difference() method.

favLangSet = {"Python", "JS", "Java", "RUST"}
PopularLangTuple = ("C", "C++", "Python", "Java")
knownList = ["Python", "Java", "HTML", "JS"]

# Tuple difference with List :

unknwonLang = favLangSet.difference(knownList)
print(unknwonLang)

# Use the difference_update() method to keep the items that are not present in both sets:
naturalNumber.difference_update(oddNumber)
print(f"The Even Number are : {naturalNumber}")