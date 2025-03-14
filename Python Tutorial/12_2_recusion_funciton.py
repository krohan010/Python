# Recursion is the process that used in function for calling themself again and again:

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

# Factorial program :
def factorial(n):
  if(n == 0 or n ==1):
    return 1
  else:
    return n * factorial(n-1)

fact = factorial(5)
print("Factorial : ", fact)