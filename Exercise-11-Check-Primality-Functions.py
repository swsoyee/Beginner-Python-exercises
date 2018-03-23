'''
Exercise 11: Check Primality Functions

Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no
divisors.). You can (and should!) use your answer to Exercise 4 to help
you. Take this opportunity to practice using functions, described below.

'''

# Solution
def divisors(number):
    divisors = [i for i in range(2, number) if number % i == 0]
    return divisors

while True:
    input_number = input('Input your number to check primality, type "exit" to exit the program:')
    if input_number.lower() == "exit":
        break
    try:
        input_number = int(input_number)
        divisors_of_input_number = divisors(input_number)
        print('Your input is primality' if len(divisors_of_input_number) == 0 else 'Your input is not primality')
    except:
        print('Input error')
        continue
