# 📌 TASK 8: School Store Purchase
# 🔹 Scenario:

# Mia needs 5 notebooks, and each costs $4.

# ✅ Fix the broken code:

# #Fix the below code
# price = "4"
# quantity = 5
# total = price * quantity  #Wrong output!
# print("Total cost:", total)


price = "4"
price = int(price)                  # Typecasting : text to int
quantity = 5
total = price * quantity            # both variable must be integer
print("Total cost:", total)