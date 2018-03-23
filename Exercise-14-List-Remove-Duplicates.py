'''
Exercise 14: List Remove Duplicates
Write a program (function!) that takes a list and returns a new
list that contains all the elements of the first list minus all
the duplicates.

Extras:

Write two different functions to do this - one using a loop and
constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for
that in a different function.

'''

# Solution
def remove_dup_loop(input_list):
    """
    Remove all duplicates in list. Using loop method.
    
    Arguments:
    input_list -- a list input
    
    Returns:
    new_list -- a list remove all the duplicates.
    """
    new_list = []
    new_list.extend(i for i in input_list if i not in new_list)
    return new_list
    

def remove_dup_set(input_list):
    """
    Remove all duplicates in list. Using set method.
    
    Arguments:
    input_list -- a list input
    
    Returns:
    new_list -- a list remove all the duplicates.
    """
    return list(set(input_list))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(remove_dup_loop(a))
print(remove_dup_set(a))
