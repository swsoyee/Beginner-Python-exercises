'''
Exercise 15: Reverse Word Order
Write a program (using functions!) that asks the user for
a long string containing multiple words. Print back to the
user the same string, except with the words in backwards
order. For example, say I type the string:

  My name is Michele
  
Then I would see the string:

  Michele is name My
  
shown back to me.

'''

# Solution
def reverse_word(string):
    """
    Reverse the input string.
    
    Arguments:
    string -- a list of input string.
    
    Returns:
    reverse_string -- a string reverse word of input string.
    """
    return ' '.join(string.split(' ')[::-1])
    
# Test Part
print(reverse_word(input('Please input a sentence:')))
