# 📌 TASK 4: Who Scored Higher? (Comparison Operators)
# 🔹 Scenario:

# Alex and Jake had a friendly math quiz. Alex scored 85 points, and Jake scored 92 points.

# 📝 Your Task:

# Use comparison operators to check:

# Who scored higher?

# Did both get the same score?

# Print the results.

# ✅ Expected Output:

# Did Alex score higher? False

# Did Jake score higher? True

# Did they both score the same? False

# ***Solution***
alex_score = 85
jake_score = 92

print("Did Alex score higher?", bool(alex_score > jake_score))
print("Did Jake score higher?", bool(jake_score > alex_score))
print("Did they both score the same?", bool(alex_score == jake_score))