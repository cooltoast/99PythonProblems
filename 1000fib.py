import math

found_num = False
n2 = 5
n1 = 8
num = 0
term = 5
while (found_num == False):
  if (len(str(n1)) >= 1000):
    found_num = True
    num = term

  x = n1  
  n1 = n1 + n2  
  n2 = x
  term += 1

print term 