'''
Exercise 12: List Ends

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. For
practice, write this code inside a function.

'''

# Solution
a = [5, 10, 15, 20, 25]

def first_last(input_list):
    return [input_list[0], input_list[-1]]

print(first_last(a))
