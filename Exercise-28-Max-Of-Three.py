'''
Exercise 28: Max Of Three

Implement a function that takes as input three variables, and
returns the largest of the three. Do this without using the Python
max() function!

The goal of this exercise is to think about some internals that
Python normally takes care of for us. All you need is some
variables and if statements!

'''

# Solution
def get_input():
    """
    Get the user input number, split by space.

    Returns:
    input_number -- a list contain all the numbers of user's input
    """
    input_number = input('Please type some numbers, split by space:').split()
    try:
        input_number = [float(i) for i in input_number]
    except ValueError:
        print('Input error')
        input_number = []
    return input_number

def get_max(input_number):
    """
    Get the max value in input_numebr list.
    
    Arguments:
    input_number -- a list contain all the numbers of user's input
    
    Returns:
    max_value -- the max value in input_numebr list.
    """
    max = float('-inf')
    for i in input_number:
        max = i if i > max else max
    if len(input_number) == 0:
        max = 'Please check your input'
    return max
    
def main():
    input_number = get_input()
    print(get_max(input_number))
    
if __name__ == "__main__":
    main()
