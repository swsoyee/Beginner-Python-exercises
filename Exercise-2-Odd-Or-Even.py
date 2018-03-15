'''
Exercise 2: Odd Or Even

Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one
number to divide by (check). If check divides evenly into num, tell that
to the user. If not, print a different appropriate message.

'''

input_number = int(input('Please input a number (num):'))
input_check = int(input('Please input a check number (check):'))

result_message = "Your input is an even number." if input_number % 2 == 0 else "Your input is an odd number."
result_message += "\nYour input is a multiple of 4." if input_number % 4 == 0 else ""
number_divided = "divides" if input_number % input_check == 0 else "dose not divide"
result_message += "\nYour input number {yes_or_not} evenly by {check}".format(yes_or_not = number_divided, check = input_check)
print(result_message)
