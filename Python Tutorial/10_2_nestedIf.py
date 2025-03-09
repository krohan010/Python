a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

if a > b:
    if a > c :
        print("a is greater than b & c")
    else:
        print("c is greater than b & a")
else:
    if b > c:
        print("b is greater than a & c")
    else:
        print("c is greater than b & a")


# pass statement to avoid getting an error :
if a > b:
    pass