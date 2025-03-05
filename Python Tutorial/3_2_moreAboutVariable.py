#Assign multiple values to the variable....
# no of variables should be equivalant to no of values
x, y, z = 10, 20, 30
print(x)
print(y)
print(z)

# One value assign to multiple variable...
x = y = z = 100
print(x)
print(y)
print(z)

#Unpacking -> The process of extracting values into variables from list or tuple(Stores collection of values)..
name = ["Rahul", "Sumit", "Simran", "Sameer"]
x1 , x2, x3, x4= name
print(x1, x2, x3, x4)  #print multiple output seperated by comma
print(x1 + " is student of RPVV school") #here plus symbol used to concatenate strings


