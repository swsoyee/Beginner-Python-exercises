'''
Exercise 23: File Overlap

Given two .txt files that have lists of numbers in them, find the
numbers that are overlapping. One .txt file has a list of all prime
numbers under 1000, and the other .txt file has a list of happy
numbers up to 1000.

'''
# Solution
def read_file(filename):
    """
    Read a text file and store all lines into a list.
    
    Arguments:
    filename -- file name.
    
    Returns:
    lines -- a list contain all lines in the file.
    """
    with open(filename, 'r') as open_file:
        lines = open_file.read().splitlines()
    return lines

def main():
    file1 = map(int, read_file('primenumbers.txt'))
    file2 = map(int, read_file('happynumbers.txt'))
    overlap = list(set(file1) & set(file2))
    print(sorted(overlap))
        
if __name__ == "__main__":
    main()

# Test Part
# >>> %Run test.py
# [7, 13, 19, 23, 31, 79, 97, 103, 109, 139, 167, 193, 239, 263, 293, 313, 331, 367, 379, 383, 397, 409, 487, 563, 617, 653, 673, 683, 709, 739, 761, 863, 881, 907, 937]
