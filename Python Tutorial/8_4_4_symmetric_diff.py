# The Symmetric_difference() method will keep the items which are not present in both :

favLang = {"Python", "JS", "Java", "RUST"}
PopularLang = {"C", "C++", "Python", "Java"}
knownLang = {"Python", "Java", "HTML", "JS"}

best_comb = favLang.symmetric_difference(knownLang)
print(best_comb)

# ^ operator used instead of symmetric_difference() :

another_comb = knownLang ^ favLang
print(another_comb)

# Note: The ^ operator only allows you to join sets with sets, and not with other data types
# like you can with the symmetric_difference() method.

most_demanding_lang = ("Python", "Java", "HTML", "JS", "VB script")             # tuple

anotner_one_comb = favLang.symmetric_difference(most_demanding_lang)            # combination with tuple
print(anotner_one_comb)

# The symmetric_difference_update() method will also keep all but the duplicates,
# but it will change the original set instead of returning a new set.

favLang.symmetric_difference_update(most_demanding_lang)
print(favLang)
