import math

def isPrime (n):
  if (n <= 1): 
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if (n % i == 0):
      return False   
  return True

primes = [2,3,5,7,11,13,17,19,23,27,29]

num = 31;

while (len(primes) <= 10001):
	if (isPrime(num)):
		primes.append(num)
	num = num + 1
	
print primes[-1]		