# Function : is a block of code that runs when is called :

# In Python a function is defined using the def keyword:

def myFunction():
    print("Hello World!")

myFunction()

# Parameters & Arguments : Both are used for passing information into function using parameters & arguments.

# Parameters : The information stored into the variable inside of function.
# Arguments : The information passed from is called parameter.

def sayHello(name):                        # Parameter : name
    print("Hello "+name)

sayHello("Rohan")                           # Arguments : Rohan
sayHello("Sumit")

# More thatn one Arguments :
def sayHelloWithFullName(fname, lname):
    print("Hello", fname, lname)


sayHelloWithFullName("Rohan", "choudhary")


# Arbitrary Arguments args* :
# when you don't know how many numbers of arguments passed to a function (Dynamically no of arguments to be passed)
# The function will receive a tuple of parameters.

def allNames(*names):
    for name in names:
        print(name)

allNames("Rimjhim", "Gayetri", "Dristhi", "Simran")

# send arguments with key = value pair :
def keyValue(third, first, second):
    print(f"First person : {first} \nSecond person : {second} \nThird person : {third}")

keyValue(first="Anuj", second="Gaurav", third="Nidhi")

# Arbitrary Keyword arguments :
# when you dont know how many keys and values passed throught the arguments :
# This function will receive dictionary of arguments.

def arbitrarykeyvalue(**person):
    for key in person:
        print(f"{key} : {person[key]}")

arbitrarykeyvalue(fname1="Rohan", lname1="kumar", fname2="Anish", lname2="verma")

# Default Parameter value :
# If we call the function without argument, it uses the default value.

def defFunction(winCountry = "India"):
    print(f"{winCountry} win the match of 2025")

defFunction()
defFunction("New zealand")

# parameter as List
def returnList(fruit):
    print(fruit)

returnList(["Apple", "Mango", "Banana", "Strawberry"])

# The pass statement :
def passFunction():
    pass

print("This is an pass function which return nothing :", passFunction())