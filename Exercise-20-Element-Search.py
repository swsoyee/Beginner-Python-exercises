'''
Exercise 20: Element Search

Write a function that takes an ordered list of numbers (a list
where the elements are in order from smallest to largest) and
another number. The function decides whether or not the given
number is inside the list and returns (then prints) an
appropriate boolean.

Extras:
Use binary search.

'''

# Solution
def search_in_simple(number_list, query):
    """
    Search query in number_list or not.
    
    Arguments:
    number_list -- a list contain all the elements.
    query -- a element
    
    Returns:
    True/False -- if query in number_list return True, else return False
    """
    if query in number_list:
        return True
    else:
        return False

def search_in_binary(number_list, start, end, query):
    """
    Search query in number_list or not.
    
    Arguments:
    number_list -- a list contain all the elements.
    start -- start index.
    end -- end index.
    query -- a element.
    
    Returns:
    True/False -- if query in number_list return True, else return False
    """
    if start > end:
        return False
    mid = int(start + (end - start) / 2)
    if number_list[mid] > query:
        return search_in_binary(number_list, start, mid - 1, query)
    if number_list[mid] < query:
        return search_in_binary(number_list, mid + 1, end, query)
    return True
    
def main():
    number_list = [1, 2, 3, 4, 6, 7, 8, 9]
    query1 = 4
    query2 = 5
    print(search_in_simple(number_list, query1))
    print(search_in_binary(number_list, 0, len(number_list), query1))
    print(search_in_simple(number_list, query2))
    print(search_in_binary(number_list, 0, len(number_list), query2))
    
if __name__ == "__main__":
    main()
