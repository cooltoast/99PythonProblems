def list_sum(a_list):
  sum_list = 0
  for n in a_list:
    sum_list = sum_list + n
  return sum_list


def is_abundant(n):
  proper_divisors = []
  is_abundant = False  
  for i in range(1, n/2 + 1):
    if (n % i == 0):
      proper_divisors.append(i)
  if (list_sum(proper_divisors) > n):
    return True
  else:
    return False

abundant_numbers = [12]
sum_of_abundant_numbers = [24]
sum_sum_of_abundant_numbers = 0

sum_sum_of_abundant_numbers_index = 1


for i in range(13, 28124):
  if (is_abundant(i)):
    abundant_numbers.append(i)




for num in range(25, 28124):
  found_abundant_sum = False
  for i in range(0, len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
      if (found_abundant_sum == False and abundant_numbers[i] + abundant_numbers[j] == num):
        sum_of_abundant_numbers.insert(sum_sum_of_abundant_numbers_index, num)
        sum_sum_of_abundant_numbers_index  = sum_sum_of_abundant_numbers_index + 1
        found_abundant_sum = True

        

print (28123 * (28124 / 2)) - list_sum(sum_of_abundant_numbers)        