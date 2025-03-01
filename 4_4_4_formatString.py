# F-String introduced in python 3.6 and now the preffered way to formatting string

lang = "Python"   #change the literal(value)....then in the desc also change....
# it works as a placeholder in the description...
desc_lang = f"{lang} is the most popular language in the world."
print(desc_lang)

#Display the price with 2 decimal points...
price = 1200
print(f"The Noise headphone is worth at rs {price : .2f} and it looks good")