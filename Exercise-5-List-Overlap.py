'''
Exercise 5: List Overlap 

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this
out at this point - we’ll get to it soon)

'''
import random
# Solution
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = [int(10 * random.random()) for i in range(20)]
b = [int(10 * random.random()) for i in range(15)]
print("List 1: ", a)
print("List 2: ", b)
print("Overlap: ", list(set(a).intersection(b)))
