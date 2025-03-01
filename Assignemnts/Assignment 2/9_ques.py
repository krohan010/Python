# 📌 TASK 9: Age Comparison Game! (Comparison + Logical Operators)
# 🔹 Scenario:

# Mia and Jake want to compare their ages and see who is older!

# 📝 Your Task:

# Ask for Mia’s and Jake’s ages.

# Use comparison & logical operators to print who is older, younger, or if they are the same age.

# ***Solution***
mia_age = input("Enter Mia's Age : ")
jake_age = input("Enter Jake's Age : ")

if(mia_age > jake_age):
    print("Mia is Older than Jake")
elif(mia_age < jake_age):
    print("Mia is younger than Jake")
else:
    print("Both age are same")