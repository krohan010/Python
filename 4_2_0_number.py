# There are 3 numeric data types : 
num = 978  #int
num1 = 10.5  #float
num2 = 1j  #complex

# To check its data types..
# print(type(num))
# print(type(num1))
# print(type(num2))

# Integer...
# nt, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 123456789012456845
z = -456
print(type(x))
print(type(y))
print(type(z))

# Float...
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 1.23
# x = 35e3
y = 1.0
# y = 12E4
z = -1.205
# z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

# complex...
# Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

# Type Conversion
x = 12
y = 11.8
z = 20j

a = float(x)
b = int(y)
c = complex(x)

print(a, b, c)
print(type(a), type(b), type(c))