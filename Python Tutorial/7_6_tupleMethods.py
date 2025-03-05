# Methods of tuples are :

# COUNT() : Returns the number of times a specified value occurs in a tuple
numTuple = (1,3,5,7,9, 7, 8, 2, 7, 6, 5, 3)
strTuple = ("A", "b", "A", "a", "C", "c")
print(f"The no. of times 7 is repeated in the tuple is : {numTuple.count(7)}")
print(f"The no. of times A is repeated in the tuple is : {strTuple.count("A")}")

# INDEX() : Searches the tuple for a specified value and returns the position of where it was found
print(f"The 9 value at {numTuple.index(9)} position")
# it returns the index of first occurrence in the list