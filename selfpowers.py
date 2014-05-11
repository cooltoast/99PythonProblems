import math

num = 0

for i in range(1, 1001):
  x = i ** i
  n = (x % 10000000000)
  num = num + n

print num