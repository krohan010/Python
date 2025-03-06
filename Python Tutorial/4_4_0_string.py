import random
# String -> surrounded by either single quotation marks, or double quotation marks.
# print('hello world')
# print("It's Alright")  

txt = "Good Morning!"
# print(txt)

# Assign multiple string to the variable..
mulstr = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(mulstr)

# String in python work as array & it started from 0..
# print(mulstr[1])
# rand = mulstr.randrange(0, 50)
print(mulstr[random.randrange(0, 50)])

# Print String Array using loop
# for x in "Banana":
#     print(x)

# To get length of an variable...
randtxt = "Hello World"
print(len(randtxt))

intro = "Hello All, myself Rohan. How are you doing?"
#if text found then...
# print("Rohan" in intro)
if "Rohan" in intro:
    print("Text Founded")

# If text not found...
# print("Kumar" not in intro)
if "Kumar" not in intro:
    print("Not founded")
