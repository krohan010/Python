# You can access the items of a dictionary by referring its key name, inside square brackets :

car = {
    "brand" :   "Ford",
    "Model" :   "Mustang",
    "electric"   :   False,
    "year"  :   1990,
    "Colors" :   ["Red", "Blue", "Black"]
}
print(car["Model"])

x = car["Model"]
# x = car.get("Model")
print(car.get("brand"))
print(x)

# key() method : To get all the key into a list :
allKeys = car.keys()
print(allKeys)                          # Dictionary keys
print(type(allKeys))                    # Data types : dict_keys

car["height"] = "5ft"
print(allKeys)                          # return the update key names list

# values() method : to get all values from the dictionary :
allValue = car.values()
print(allValue)
print(type(allValue))                      # data type : dict_values

car["year"] = 2020
print(allValue)                            # return the updated values list

# The items() method returns each item in a dictionary from another dictionary :
car2 = car.items()
print(car2)                 # before added

car["royal"] = True
print(car2)                 # After added one item