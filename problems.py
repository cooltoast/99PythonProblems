import math
import random
import itertools

#Problem 1
print "~~~~~~~~~~~ PROBLEM 1 ~~~~~~~~~~~~~"
def last (some_list):
  if not some_list:
    return None
  return some_list[-1]

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
assert(last(a_list) is 7)

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
assert(last(another_list) is 'f')


#Problem 2
print "~~~~~~~~~~~ PROBLEM 2 ~~~~~~~~~~~~~"
def penultimate (some_list):
  if len(some_list) <= 1:
    return None
  return some_list[-2]

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
assert(penultimate(a_list) is 6)

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
assert(penultimate(another_list) is 'e')


#Problem 3
print "~~~~~~~~~~~ PROBLEM 3 ~~~~~~~~~~~~~"
def element_at (some_list, index):
  # problem stated convention that k=1 returns first element
  return some_list[index - 1]

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
assert(element_at(a_list, 3) is 2)

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
assert(element_at(another_list, 1) is 'a')


#Problem 4
print "~~~~~~~~~~~ PROBLEM 4 ~~~~~~~~~~~~~"
def count (some_list):
  #print len(some_list)
  #^too easy

  length = 0
  for i in some_list:
  	length += 1
  return length

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
assert(count(a_list) is len(a_list))

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
assert(count(another_list) is len(another_list))


#Problem 5
print "~~~~~~~~~~~ PROBLEM 5 ~~~~~~~~~~~~~"
def reverse (some_list):
  temp = []
  for x in some_list:
    temp = [x] + temp
  return temp

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
assert(reverse(a_list) == a_list[::-1])

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
assert(reverse(another_list) == another_list[::-1])


#Problem 6
print "~~~~~~~~~~~ PROBLEM 6 ~~~~~~~~~~~~~"
def is_palindrome (some_list):
  for index in xrange(len(some_list)/2):
    if (some_list[index] != some_list[len(some_list) - 1 - index]):
      return False
  return True

a_list = ['s', 'p', 'a', 'm']
assert(is_palindrome(a_list) == False)

another_list = ['k', 'a', 'y', 'a', 'k']
assert(is_palindrome(another_list) == True)


another_list = [1, 2, 3, 2, 1]
assert(is_palindrome(another_list) == True)


#Problem 7
print "~~~~~~~~~~~ PROBLEM 7 ~~~~~~~~~~~~~"
def flatten(some_list, flat_list):   
  for i in some_list:
      if isinstance(i, list):
          flatten(i, flat_list)
      else:
          flat_list.append(i)
  return flat_list

a_list = [0, 1, [2, [3]], [[[[4]]]], 5, [6, 7], [8,[9,[10]]]]
b_list = [[[[[0]]]],[1,2,3],[4,5,6], [7], [8,9], 10]

assert(flatten(a_list, []) == range(11))
assert(flatten(b_list, []) == range(11))

#Problem 8
print "~~~~~~~~~~~ PROBLEM 8 ~~~~~~~~~~~~~"
def compress(a_list):
  for i in xrange(len(a_list)):
    for j in xrange(len(a_list) - 1, i, -1):
      if (a_list[i] == a_list[j]):
        a_list.remove(a_list[j])

  return a_list

print compress([1, 1, 2, 1, 2, 3, 4, 4, 5, 6, 3, 5, 7, 8, 9, 10, 10])


#Problem 9
print "~~~~~~~~~~~ PROBLEM 9 ~~~~~~~~~~~~~"
def pack(a_list):
  if not a_list:
    return a_list

  packed_list = []
  i = 0
  while(i < len(a_list)):
    sub_list = []
    j = i + 1
    while(j < len(a_list) and a_list[i] == a_list[j]):
      sub_list.append(a_list[j])
      j += 1
    if sub_list:
      sub_list.append(a_list[i])
      packed_list.append(sub_list)
    else:
      packed_list.append(a_list[i])
    i = j
  return packed_list


assert(pack([1,1,1,4,45,632,4,7,45,34]) == [[1,1,1],4,45,632,4,7,45,34])
assert(pack([1,1,2,1,2,3,4,4,5,6,3,5,7,8,9,10,10]) == [[1,1],2,1,2,3,[4,4],5,6,3,5,7,8,9,[10,10]])
assert(pack(range(10)) == range(10))

#work on lists to do problems 7-30 


#Problem 14
print "~~~~~~~~~~~ PROBLEM 14 ~~~~~~~~~~~~~"
def duplicate (some_list):
  duplicate_list = []
  for i in some_list:
    duplicate_list.append(i) 
    duplicate_list.append(i)
  return duplicate_list  

assert(duplicate(range(10)) == [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9])


#Problem 15
print "~~~~~~~~~~~ PROBLEM 15 ~~~~~~~~~~~~~"
def replicate (some_list, n):
  duplicate_list = []
  for i in some_list:
    for index in xrange(n):
      duplicate_list.append(i) 
  return duplicate_list  

assert(replicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) ==
       [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10])


#Problem 16
print "~~~~~~~~~~~ PROBLEM 16 ~~~~~~~~~~~~~"
def drop (some_list, n):
  for i in range(n - 1, len(some_list), n):
    some_list[i] = "~~~~~~~~~~****remove me!****~~~~~~~~~~"
  for element in some_list:  
    if element == "~~~~~~~~~~****remove me!****~~~~~~~~~~":
      some_list.remove(element)
  return some_list  

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert(drop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) ==  [1, 3, 5, 7, 9])
assert(drop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [1, 2, 4, 5, 7, 8, 10])
assert(drop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) == [1, 2, 3, 5, 6, 7, 9, 10])
assert(drop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == [1, 2, 3, 4, 6, 7, 8, 9])
assert(drop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6) == [1, 2, 3, 4, 5, 7, 8, 9, 10])
assert(drop(a_list, 2) == [1, 3, 5, 7, 9])
assert(drop(a_list, 3) == [1, 3, 7, 9])
assert(drop(a_list, 4) == [1, 3, 7])


#Problem 17
print "~~~~~~~~~~~ PROBLEM 17 ~~~~~~~~~~~~~"
def split_list (some_list, n):
  return some_list[:n], some_list[n:]   

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert(split_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == ([1, 2, 3], [4, 5, 6, 7, 8, 9, 10]))
assert(split_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) == ([1, 2, 3, 4], [5, 6, 7, 8, 9, 10]))
assert(split_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
assert(split_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6) == ([1, 2, 3, 4, 5, 6], [7, 8, 9, 10]))
assert(split_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7) == ([1, 2, 3, 4, 5, 6, 7], [8, 9, 10]))


#Problem 18
print "~~~~~~~~~~~ PROBLEM 18 ~~~~~~~~~~~~~"
def slice(some_list, I, K):
  return some_list[I - 1:K]

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert(slice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 6) == [3, 4, 5, 6])
assert(slice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 7) == [1, 2, 3, 4, 5, 6, 7])
assert(slice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6, 10) == [6, 7, 8, 9, 10])
assert(slice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, 8) == [4, 5, 6, 7, 8])


#Problem 19
print "~~~~~~~~~~~ PROBLEM 19 ~~~~~~~~~~~~~"
def rotate(some_list, n):
  temp_list = some_list[n:]
  return temp_list + some_list[:n]

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert(rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [4, 5, 6, 7, 8, 9, 10, 1, 2, 3])
assert(rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6) == [7, 8, 9, 10, 1, 2, 3, 4, 5, 6])
assert(rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9) == [10, 1, 2, 3, 4, 5, 6, 7, 8, 9])
assert(rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [3, 4, 5, 6, 7, 8, 9, 10, 1, 2])


#Problem 20
print "~~~~~~~~~~~ PROBLEM 20 ~~~~~~~~~~~~~"
def remove_at (some_list, n):
  element_to_rm = some_list[n - 1]
  some_list.remove(element_to_rm)
  return some_list  

a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert(remove_at([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == [0, 2, 3, 4, 5, 6, 7, 8, 9])
assert(remove_at([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [0, 1, 3, 4, 5, 6, 7, 8, 9])
assert(remove_at([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4) == [0, 1, 2, 4, 5, 6, 7, 8, 9])
assert(remove_at(a_list, 2) == [0, 2, 3, 4, 5, 6, 7, 8, 9])
assert(remove_at(a_list, 3) == [0, 2, 4, 5, 6, 7, 8, 9])
assert(remove_at(a_list, 4) == [0, 2, 4, 6, 7, 8, 9])
assert(remove_at(a_list, 5) == [0, 2, 4, 6, 8, 9])
assert(remove_at(a_list, 6) == [0, 2, 4, 6, 8])


#Problem 21
print "~~~~~~~~~~~ PROBLEM 21 ~~~~~~~~~~~~~"
def insert_at (some_list, n, index):
  some_list.insert(index, n)
  return some_list
     
a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert(insert_at(a_list, 15, 2) == [0, 1, 15, 2, 3, 4, 5, 6, 7, 8, 9])
assert(insert_at(a_list, 45, 1) == [0, 45, 1, 15, 2, 3, 4, 5, 6, 7, 8, 9])
assert(insert_at(a_list, 88, 5) == [0, 45, 1, 15, 2, 88, 3, 4, 5, 6, 7, 8, 9])


#Problem 22
print "~~~~~~~~~~~ PROBLEM 22 ~~~~~~~~~~~~~"
def range_list (lower, upper):
  return range(lower, upper + 1)

assert(range_list(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert(range_list(4, 30) == [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
assert(range_list(17, 56) == [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56])



#Problem 23
print "~~~~~~~~~~~ PROBLEM 23 ~~~~~~~~~~~~~"
def rand_list (some_list, n):
  return random.sample(some_list, n)

a_list = [1,2,3,4,5,6,7,8,9,10]
print "                       Original list: ", a_list
print " Random list of 4 from Original List: ", rand_list(a_list, 4)
print " Random list of 6 from Original List: ", rand_list(a_list, 6)
print "Random list of 10 from Original List: ", rand_list(a_list, 10)


#Problem 24
print "~~~~~~~~~~~ PROBLEM 24 ~~~~~~~~~~~~~"
def lotto (N, M):
  lotto_list = []
  for i in range(0, N):
    lotto_num = random.randint(1, M)
    lotto_list.append(lotto_num)
  return lotto_list

print "Lotto List of 2 elements up to 4: ", lotto(2, 4)
print "Lotto List of 4 elements up to 10: ", lotto(4, 10)
print "Lotto List of 5 elements up to 20: ", lotto(5,20)
print "Lotto List of 10 elements up to 100: ", lotto(10, 100)


#Problem 25
print "~~~~~~~~~~~ PROBLEM 25 ~~~~~~~~~~~~~"
def rand_perm (some_list):
  return random.sample(some_list, len(some_list))

a_list = [1,2,3,4,5,6,7,8,9,10]
print "                       Original list: ", a_list
print " Random list of 4 from Original List: ", rand_perm(a_list)
print " Random list of 4 from Original List: ", rand_perm(a_list)
print " Random list of 4 from Original List: ", rand_perm(a_list)


#Problem 26
print "~~~~~~~~~~~ PROBLEM 26 ~~~~~~~~~~~~~"
def combination (some_list, K):
  return itertools.combinations(some_list, K)

a_list = [1,2,3,4,5,6,7,8,9,10]
print "                       Original list: ", a_list
print " Random list of 4 from Original List: ", combination(a_list, 3)
print " Random list of 4 from Original List: ", combination(a_list, 2)
print " Random list of 4 from Original List: ", combination(a_list, 6)


#Problem 31
print "~~~~~~~~~~~ PROBLEM 31 ~~~~~~~~~~~~"
def isPrime (n):
  if (n <= 1): 
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if (n % i == 0):
      return False
  #if we reach here, then we have found no divisors of n
  #therefore n is prime    
  return True

print isPrime(4)
print isPrime(7)
print isPrime(15)
print isPrime(19)
print isPrime(83)
print isPrime(91)
print isPrime(3571)       

#Problem 32
#recursively uses Euclid's Algorithm (http://en.wikipedia.org/wiki/Euclidean_algorithm)
print "~~~~~~~~~~~ PROBLEM 32 ~~~~~~~~~~~~"
def gcd (a, b):
  #assuming a >= b
  #swap the arguments if b > a
  if (b > a): 
    gcd (b, a)  

  #now we have ensured a >= b  

  if (a % b == 0):
    return b 

  #else a % b != 0
  return gcd(b, a % b)    
  

print "GCD of 2 & 4 is: ", gcd(2, 4) 
print "GCD of 4 & 7 is: ", gcd(4, 7)
print "GCD of 36 & 63 is: ", gcd(36, 63)
print "GCD of 12 & 1032 is: ", gcd(12, 1032)
print "GCD of 1785 & 546 is: ", gcd(1785, 546)
print "GCD of 31415926534676736647 & 438478473847834834784748 is: ", gcd(31415926534676736647, 438478473847834834784748)

#Problem 33
#problem 32 makes this almost trivial
print "~~~~~~~~~~~ PROBLEM 33 ~~~~~~~~~~~~"
def coprime (a, b):
  if (gcd(a, b) == 1):    
    return True
  return False

print "Are 2 & 4 coprime? ", coprime(2, 4) 
print "Are 4 & 7 coprime? ", coprime(4, 7)
print "Are 36 & 5 coprime? ", coprime(36, 5)
print "Are 11 & 1032 coprime? ", coprime(11, 1032)
print "Are 1785 & 546 coprime? ", coprime(1785, 546)
print "Are 31415926534676736647 & 438478473847834834784748 coprime? ", coprime(31415926534676736647, 438478473847834834784748)


#Problem 34
#computes the totient function of n (http://en.wikipedia.org/wiki/Euler's_totient_function)
print "~~~~~~~~~~~ PROBLEM 34 ~~~~~~~~~~~~"
def phi (n):
  totatives = []
  for i in range(1, n + 1):
    if (coprime(n, i)):
      totatives.append(i)

  return totatives    

print "How many totatives of 1? ", len(phi(1)), phi(1)
print "How many totatives of 9? ", len(phi(9)), phi(9)
print "How many totatives of 10? ", len(phi(10)), phi(10)
print "How many totatives of 15? ", len(phi(15)), phi(15)
print "How many totatives of 24? ", len(phi(24)), phi(24)
print "How many totatives of 36? ", len(phi(36)), phi(36)

#Problem 35

print "~~~~~~~~~~~ PROBLEM 35 ~~~~~~~~~~~~"
def prime_factors (n):
  prime_factors = []

  #easy basic case
  if (isPrime(n)):
    prime_factors.append(n)
    return prime_factors

  #find all primes up to n/2  
  #check for divisibilty, append to a list if true
  for i in range (2, n/2 + 1):
    while (isPrime(i) and n % i == 0):
      prime_factors.append(i)
      n = n/i

  return prime_factors   

print "Prime factors of 7 are: ", prime_factors(7)
print "Prime factors of 15 are: ", prime_factors(15)
print "Prime factors of 34 are: ", prime_factors(34)
print "Prime factors of 12 are: ", prime_factors(12)
print "Prime factors of 24 are: ", prime_factors(24)
print "Prime factors of 144 are: ", prime_factors(144)
print "Prime factors of 43735 are: ", prime_factors(43735)


#Problem 36

print "~~~~~~~~~~~ PROBLEM 36 ~~~~~~~~~~~~"
def prime_factors_mult (n):

  prime_factors_mult = []

  #easy basic case
  if (isPrime(n)):
    prime_factors_mult.append(n)
    return prime_factors_mult

  list_of_possible_prime_factors = []
  
  for i in range(2, n/2 + 1):
    if (isPrime(i)):
      list_of_possible_prime_factors.append(i)

  #check for divisibilty, append to a list if true
  for prime in list_of_possible_prime_factors:
    factor_mult = []
    factor_counter = 0
    while (n % prime == 0):
      n = n/prime
      factor_counter = factor_counter + 1
    if (factor_counter > 0):
      factor_mult = [prime, factor_counter]
      prime_factors_mult.append(factor_mult)  
  return prime_factors_mult


print "Prime factorization of n: [[prime_factor, #_times_factor_occurs], ...]"
print "Prime factorization of 7 is: ", prime_factors_mult(7)
print "Prime factorization of 15 is: ", prime_factors_mult(15)
print "Prime factorization of 34 is: ", prime_factors_mult(34)
print "Prime factorization of 12 is: ", prime_factors_mult(12)
print "Prime factorization of 24 is: ", prime_factors_mult(24)
print "Prime factorization of 144 is: ", prime_factors_mult(144)
print "Prime factorization of 43735 is: ", prime_factors_mult(43735)


#Problem 39
#prints primes such that lower <= primes[] <= upper
print "~~~~~~~~~~~ PROBLEM 39 ~~~~~~~~~~~~"
def primelist (lower, upper):
  #if upper is <2, then we can't list any primes
  if (upper < 2):
    return

  primelist = []  

  for i in range(lower, upper + 1):
    if (isPrime(i)):
      primelist.append(i)  
      
  return primelist

print "Primes btwn -345 and 1 inclusive: ", primelist(-345, 1)
print "Primes btwn 23 and 57 inclusive: ", primelist(23, 57)
print "Primes btwn 11 and 67 inclusive: ", primelist(11, 67)
print "Primes btwn 10 and 30 inclusive: ", primelist(10, 30)
print "Primes btwn 0 and 100 inclusive: ", primelist(0, 100)


#Problem 40
#problem asks to print one goldbach composition possibilty for an even number
#screw that, I'm going to print all possibilities for any integer

#Every even integer greater than 2 can be expressed as the sum of two primes.
#Every odd number greater than 5 can be expressed as the sum of three primes. 
#(A prime may be used more than once in the same sum.)

#prints all possible goldbach compositions of a number (http://en.wikipedia.org/wiki/Goldbach's_conjecture)
print "~~~~~~~~~~~ PROBLEM 40 ~~~~~~~~~~~~"

def goldbach (n):
  
  #any integer 3 or below have no goldbach composition
  #5 also has no goldbach composition
  #4,6,7,8,....,infinity all have goldbach composition
  if (n <= 3 or n == 5): 
    return

  #n must be > 3 now

  goldbach_list = []
  goldbach_set = []
  list_of_primes = primelist(0, n/2)  
  #^generate primes up to n/2, inclusive

  if (n % 2 == 0):
    for prime in list_of_primes:
      if (isPrime(n - prime)):
        goldbach_set = [prime, n - prime]
        goldbach_list.append(goldbach_set)

  else: #n is odd
    for prime in list_of_primes:
      if ((n - prime) % 2 == 0):
        goldbach_list = goldbach(n - prime) + [prime]
        goldbach_list.sort()
      elif (isPrime(n - prime - 2)):
        goldbach_set = [prime, 2, n - prime - 2]
        
        #print goldbach_set
        goldbach_list.append(goldbach_set)
        #print goldbach_list
        goldbach_list.sort()

  return goldbach_list

print "Goldbach compisition of odd_num: [prime1, [prime2, prime3], [prime4, prime5], ...]"
print "where odd_num = prime1 + prime2 + prime 3 = prime1 + prime4 + prime5 = ..."
print "Goldbach composition of 1: ", goldbach(1)
print "Goldbach composition of 2: ", goldbach(2)
print "Goldbach composition of 11: ", goldbach(11)
print "Goldbach composition of 15: ", goldbach(15)
print "Goldbach composition of 28: ", goldbach(28)
print "Goldbach composition of 36: ", goldbach(36)
print "Goldbach composition of 49: ", goldbach(49)


#Problem 41
#Print goldbach composition for all even numbers greater than 'lower' and less than or equal to 'upper'
print "~~~~~~~~~~~ PROBLEM 41 ~~~~~~~~~~~~"

def goldbach_list (lower, upper):

  if (lower % 2 != 0):
    lower = lower + 1

  goldbach_list = []
  for i in range (lower, upper + 1, 2):
    print i, ": ", goldbach(i)
  
  

print "Even Goldbach compositions from 1 to 10: "
goldbach_list(1, 10)
print "Even Goldbach compositions from 5 to 16: "
goldbach_list(5, 16)
print "Even Goldbach compositions from 20 to 35: "
goldbach_list(20, 35)
print "Even Goldbach compositions from 46 to 100: "
goldbach_list(46, 100)
