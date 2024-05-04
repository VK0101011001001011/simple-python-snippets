# Check if a string is a palindrome

string = "racecar"  # Input string

# Reverse the string using slicing (efficient way to reverse in Python)
reversed_string = string[::-1] 

# Compare the original and reversed strings for equality
if string == reversed_string:
  print(string, "is a palindrome")  # A palindrome reads the same backward and forward
else:
  print(string, "is not a palindrome") 
