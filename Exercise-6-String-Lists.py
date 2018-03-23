'''
Exercise 6: String Lists
Ask the user for a string and print out whether this string is a
palindrome or not. (A palindrome is a string that reads the same
forwards and backwards.)

'''

# Solution
input_string = input("Pleas input a string:")
print("String is a palindrome" if input_string[::-1] == input_string else "String is not a palindrome")
