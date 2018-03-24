'''
Exercise 21: Write To A File

Take the code from the How To Decode A Website exercise
(if you didn’t do it or just want to play with some different
code, use the code from the solution), and instead of
printing the results to a screen, write the results to a txt
file. In your code, just make up a name for the file you are
saving to.

Extras:
Ask the user to specify the name of the output file that will
be saved.

'''

# Solution
def main():
    file_name = input('Input file name:')

    lines = ['Hello world\n', 'Hello world 2!\n', 'Hello world 3~\n']
    
    with open(file_name, 'w') as file:
        for line in lines:
            file.write(line)
    
if __name__ == "__main__":
    main()
