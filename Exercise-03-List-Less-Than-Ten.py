'''
Exercise 3: List Less Than Ten

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

1. Instead of printing the elements one by one, make a new list that has all the elements
less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from the
original list a that are smaller than that number given by the user.

'''

input_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Solution
print("Solution")

for i in input_list:
    if i < 5:
        print(i)
        
# Extras
print("Extras")

cut_off = int(input("Please input the cut off number:"))
new_list = [i for i in input_list if i < cut_off]
print(new_list)
