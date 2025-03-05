# Bitwise Operator are...

# & (And) -> sets each bit to 1 . if both bits are 1

x = 7
y = 3
z = x & y
print(z)                # return 3

""""How the calculation will be perfomed?
Ans -> Firt it convert the decimal numbers into Binary numbers
and then perform & operation and return final output """

# | (or) -> sets each bit to 1 . if one of the two bits is 1.
print(x | y)            #7

# ^ (XOR) -> sets each bit to 1. if only one of two bits is 1.
print(x ^ y)            # return 4

# ~ (NOT) -> invert all the bits. it means that it convert 1 is 0 and wise versa.
print(~y)