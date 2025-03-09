# If statement :

# Check A is bigger than B
A = int(input("Enter first value : "))
B = int(input("Enter second value : "))

# if A > B:
  #  print("A is bigger than B")             # without indentation, you will get an error

# if Shorthand :
if A > B : print("A is greater than B")


#if else statement :
# if A > B:
#     print("A is greater than B")
# else:
#     print("B is greater than or equal to A")

# IF else shorthand :
print("A is greater than B") if A>B else print("A is less than or equal to B")

# If else Ledger :
if A > B:
    print("A is greater than B")
elif A == B:
    print("A and B are equal")
else:
    print("A is less than B")
