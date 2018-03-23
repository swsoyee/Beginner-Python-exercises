'''
Exercise 13: Fibonacci

Write a program that asks the user how many Fibonnaci numbers
to generate and then generates them. Take this opportunity to
think about how you can use functions. Make sure to ask the
user to enter the number of numbers in the sequence to
generate.(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous
two numbers in the sequence. The sequence looks like this: 1, 1,
2, 3, 5, 8, 13, …)

'''

# Solution
def fibo_generate(number):
    """
    Generate fibonnaci numbers.
    
    Arguments:
    number -- how many numbers to generate
    
    Returns:
    fibo -- a list of fibonnaci numbers.
    """
    fibo = [1, 1]
    for i in range(0, number - 2):
        fibo.append(fibo[i] + fibo[i+1])
    return fibo

def check_input(number):
    """
    Gheck the input is a number or not
    
    Arguments:
    number -- Digital number.
    
    Returns:
    True/False -- if input is a number, return True, else return false.
    """
    try:
        if int(number) > 0:
            return (True, int(number))
    except:
        return False

def get_input():
    """
    Show input message and get input string.
    
    Returns:
    True/False -- if input is a number, return True, else return false.
    """
    input_number = input('How many Fibonnaci numbers do you want to generate?')
    return check_input(input_number)

# Initiation
check_status = get_input()
# Loop
while check_status[0]:
    print(fibo_generate(check_status[1]))
    # A new turn
    check_status = get_input()

# Test Part
# How many Fibonnaci numbers do you want to generate?5
# [1, 1, 2, 3, 5]
# How many Fibonnaci numbers do you want to generate?10
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
