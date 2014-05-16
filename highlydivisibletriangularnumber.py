import math

def divisors (n):
  divisors = 2;
  for i in range (2, n):
    if (n % i == 0):
      divisors = divisors + 1
  return divisors
  
num = 55
addnum = 10

while (divisors(num) <= 500):
  addnum = addnum + 1
  num = num + addnum


print num      