# Identity Operators are...

# is opertaor checks that both variable store in a same memory location using interning...

# Interning is the optimization technique used by python to reuse object for immutable
# (typically small integer and short String) to save memory and improve performance

x = 50
y = 50
# print true if both variables are the same object
print(x is y)

strArr1 = ["Apple", "Banana", "Orange"]
strArr2 = ["Apple", "Banana", "Orange"]
strArr3 = strArr1

print(strArr1 is strArr2)           # return false, becoz: it does not point same object
print(strArr1 == strArr2)           # return True
print(strArr1 is strArr3)           # return False