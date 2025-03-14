# Positional Function : it acts as a placeholder it means that order of arguments matters.

# inside of function slash(/) at end indicates that it is an positional function.

def describePerson(name, age, city, /):
    print(f"{name} is {age} years old, lives in {city}")

# Function calls :
# describePerson(age=21, name="Sakshi", city="Delhi")             #Throws error in case of positional function.
describePerson("Sakshi", 21, "Delhi")


# Keyword only argument : it provides clarity of argument passing. differently work from positional function.
# Arguments like : name="Vikas", age=24, city="New Delhi"

def descPerson(*, name, age, city):
    print(f"{name} is {age} years old, lives in {city}")

descPerson(name="Vikas", age=24, city="New Delhi")

# Combine Positional-Only and Keyword-Only :
def descr_person(name, /, *, age, city):
    print(f"{name} is {age} years old, lives in {city}")

descr_person("Shrikesh", age=25, city="Gajiabaad")

