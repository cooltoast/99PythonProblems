import math

def isPrime (n):
  if (n <= 1): 
    return False
  if (n % 3 == 0):
  	return False  
  for i in range(2, int(math.sqrt(n)) + 1):
    if (n % i == 0):
      return False   
  return True

sum = 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23;

for i in range(27, 2000000, 2):
	if (isPrime(i)):
		sum = sum + i;

print sum		  