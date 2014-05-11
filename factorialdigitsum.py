import math


num = math.factorial(100)

n = str(num)

sum = 0

for digit in n:
  sum = sum + int(digit)

print sum