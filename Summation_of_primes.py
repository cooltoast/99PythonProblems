import math

def isPrime (n):
  if (n <= 1): 
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if (n % i == 0):
      return False   
  return True

sum = 2;

for i in range(3, 2000000, 2):
	if (isPrime(i)):
		sum = sum + i;

print sum		  