# This program calculates the factorial of a number

num = 5  # The number to find the factorial of

factorial = 1  # Initialize the factorial with 1 (important for the calculation)

# Iterate from 1 to the number (inclusive)
for i in range(1, num + 1):
  # Update the factorial by multiplying it with the current loop value 
  factorial *= i

# Print the calculated factorial 
print("Factorial of", num, "is", factorial)
