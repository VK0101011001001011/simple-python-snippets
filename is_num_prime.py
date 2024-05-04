# Prime number checker

num = 17  # The number to check for primality

# Check if the number is greater than 1 (definition of prime numbers)
if num > 1:

  # Iterate from 2 up to half the number (optimization for prime checking)
  for i in range(2, int(num/2) + 1):

    # Check for divisibility by any number in the loop
    if (num % i) == 0: 
      print(num, "is not prime")  # If divisible, it's not prime
      break  # Exit the loop, no need to check further

  # If the loop completes without finding divisors, the number is prime
  else:
    print(num, "is prime") 

# Numbers less than or equal to 1 are not prime
else:
  print(num, "is not prime") 

