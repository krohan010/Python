# Sets are unchangeable. but we can add new value into set :

fruitSet = {"Apple", "Mango", "Banana", "Strawberry"}
fruitSet.add("Kiwi")
print(fruitSet)

# Update() method used to add another set into the current set
updateSet = {"Papaya", "Orange"}
updateSet1 = {"Papaya", "Orange", "Apple", "Mango"}
fruitSet.update(updateSet)                      # Add value of updateSet into fruitSet
print(fruitSet)

fruitSet.update(updateSet1)                     # union operation : ignore duplicate values
print(fruitSet)                                 # same output as previous

# Update() method can also add any iterable object (tuples, lists) into set
vegList = ["cauliflower", "Tomato", "Potato", "Cucumber", "Radish"]     #list
fruitSet.update(vegList)                # Adding list into set
print(fruitSet)