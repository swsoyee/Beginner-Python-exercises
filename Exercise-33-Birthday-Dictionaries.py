'''
Exercise 33: Birthday Dictionaries

This exercise is Part 1 of 4 of the birthday data exercise series.
The other exercises are: Part 2, Part 3, and Part 4.

For this exercise, we will keep track of when our friend’s birthdays
are, and be able to find that information based on their name.
Create a dictionary (in your file) of names and birthdays. When you
run your program it should ask the user to enter a name, and return
the birthday of that person back to them. The interaction should
look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
Happy coding!

'''
# Solution
def show_all_in_dict(dict):
    """
    Print all the key in dict.
    
    Arguments:
    dict -- a dictionary needed to be print it's key.
    
    """
    print('We know the birthdays of:')
    for key in dict:
        print(key)

# Useless
def search(query, dict):
    """
    Search the person's birthday is in the dict or not.
    
    Arguments:
    query -- the name of person the user want to know.
    dict -- a dictionary needed to be print it's key.
    
    Returns:
    birthday -- the birthday of the query.
    """
    return dict[query] if query in dict else None

def main():
    Birthdays ={"Albert Einstein": "14/3/1889",
                "Bill Gates": "28/10/1955",
                "Steve Jobs": "24/2/1955"}
    print('Welcome to the birthday dictionary.')
    show_all_in_dict(Birthdays)
    query = input("Who's birthday do you want to look up?")
    result = Birthdays[query] if query in Birthdays else None
    if result == None:
        print('No Data')
    else:
        print("{}'s birthday is {}".format(query, Birthdays[query]))
    
        
if __name__ == "__main__":
    main()
    
# Test Part
# >>> %Run test.py
# Welcome to the birthday dictionary.
# We know the birthdays of:
# Albert Einstein
# Bill Gates
# Steve Jobs
# Who's birthday do you want to look up?Bill Gates
# Bill Gates's birthday is 28/10/1955
# >>> %Run test.py
# Welcome to the birthday dictionary.
# We know the birthdays of:
# Albert Einstein
# Bill Gates
# Steve Jobs
# Who's birthday do you want to look up?Soi
# No Data
