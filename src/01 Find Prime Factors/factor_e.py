import math

def find_prime_factors(n):
  factors = []
  if n == 1:
    return factors
  else:
    for i in range(2,n+1):
      while n % i == 0:
        factors.append(i)
        n = n // i
    return factors 

print(find_prime_factors(25))
    
    
  

