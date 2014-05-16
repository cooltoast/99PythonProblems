import math

#Problem 1
print "~~~~~~~~~~~ PROBLEM 1 ~~~~~~~~~~~~~"
def last (some_list):
  print some_list[len(some_list) - 1]

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
last(a_list)

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
last(another_list)


#Problem 2
print "~~~~~~~~~~~ PROBLEM 2 ~~~~~~~~~~~~~"
def penultimate (some_list):
  print some_list[len(some_list) - 2]

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
penultimate(a_list)

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
penultimate(another_list)


#Problem 3
print "~~~~~~~~~~~ PROBLEM 3 ~~~~~~~~~~~~~"
def element_at (some_list, index):
  print some_list[index - 1]
  #problem stated convention that k=1 returns first element

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
element_at(a_list, 3)

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
element_at(another_list, 1)


#Problem 4
print "~~~~~~~~~~~ PROBLEM 4 ~~~~~~~~~~~~~"
def count (some_list):
  #print len(some_list)
  #^too easy

  length = 0
  for i in some_list:
  	length += 1
  print length	

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
count(a_list)

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
count(another_list)


#Problem 5
print "~~~~~~~~~~~ PROBLEM 5 ~~~~~~~~~~~~~"
def reverse (some_list):
  some_list.reverse()
  print some_list

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
reverse(a_list)

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
reverse(another_list)


#Problem 6
print "~~~~~~~~~~~ PROBLEM 6 ~~~~~~~~~~~~~"
def is_palindrome (some_list):
  for index in range(0, len(some_list)):
    if (some_list[index] != some_list[len(some_list) - 1 - index]):
      return False
  return True

a_list = ['s', 'p', 'a', 'm']
print is_palindrome(a_list)

another_list = ['k', 'a', 'y', 'a', 'k']
print is_palindrome(another_list)


another_list = [1, 2, 3, 2, 1]
print is_palindrome(another_list)


#work on lists to do problems 7-30 


#Problem 31
print "~~~~~~~~~~~ PROBLEM 31 ~~~~~~~~~~~~"
def isPrime (n):
  print n,
  if (n == 1): 
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
  

print gcd(2, 4) 
print gcd(4, 7)
print gcd(12, 1032)
print gcd(1785, 546)
print gcd(31415926534676736647, 438478473847834834784748)