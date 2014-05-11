#Problem 1

def last (some_list):
  print some_list[len(some_list) - 1]

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
last(a_list)

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
last(another_list)


#Problem 2

def penultimate (some_list):
  print some_list[len(some_list) - 2]

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
penultimate(a_list)

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
penultimate(another_list)


#Problem 3

def element_at (some_list, index):
  print some_list[index - 1]
  #problem stated convention that k=1 returns first element

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
element_at(a_list, 3)

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
element_at(another_list, 1)


#Problem 4

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

def reverse (some_list):
  some_list.reverse()
  print some_list

a_list = [0, 1, 2, 3, 4, 5, 6, 7]
reverse(a_list)

another_list = ['a', 'b', 'c', 'd', 'e', 'f']
reverse(another_list)


