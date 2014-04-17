import math

num = "0123456789"

for i in range (10, 9999999):
  num = num + str(i)

product = int(num[1]) * int(num[10]) * int(num[100]) * int(num[1000]) * int(num[10000]) * int(num[100000]) * int(num[1000000])

print product