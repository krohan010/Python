start = "Hello Python!"

# To convert into Upper case..
print(start.upper())

# To convert into lower case..
print(start.lower())

spacetxt = "          Hello World         "
print(spacetxt)
# To removes white spaces from the beginning or the end...
txt = spacetxt.strip()
print(txt)

# To replace the characters from the variable...with all match cases...
print(txt.replace("o", "a"))

csv = "Aakash, Rahul, Shubham, Aakshi, Vidya"
# returns a list where the text between the specified separator becomes the list items..
csvList = csv.split(",")
# print(csvList[0:3])
for x in csvList:
    print(x.strip())   #here split method removes the whitespace from the starting..

