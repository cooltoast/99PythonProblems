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
