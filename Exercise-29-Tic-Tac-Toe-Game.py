'''
Exercise 29: Tic Tac Toe Game

This exercise is Part 4 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 1, Part 2, and Part 3.

In 3 previous exercises, we built up a few components needed to
build a Tic Tac Toe game in Python:

Draw the Tic Tac Toe game board
Checking whether a game board has a winner
Handle a player move from user input
The next step is to put all these three components together to
make a two-player Tic Tac Toe game! Your challenge in this
exercise is to use the functions from those previous exercises
all together in the same program to make a two-player game that
you can play with a friend. There are a lot of choices you will
have to make when completing this exercise, so you can go as
far or as little as you want with it.

Here are a few things to keep in mind:

You should keep track of who won - if there is a winner, show a
congratulatory message on the screen.
If there are no more moves left, don’t ask for the next player’s
move!
As a bonus, you can ask the players if they want to play again
and keep a running tally of who won more - Player 1 or Player 2.

'''

# Solution
def check_winner(input_list, size):
    """
    Check the winner number in row, column, or diagonal direction.

    Arguments:
    input_list -- a two dimensional list for checking.
    size -- the length for winning.
    
    Returns:
    winner -- the winner player number, if no winner return None.
    
    """
    # Check row
    winner = check_row_winner(input_list, size)
    if winner == None:
        # Transpose matrix
        input_list = transpose(input_list)
        # Check column
        winner = check_row_winner(input_list, size)
    if winner == None:
        # Check diagnal
        winner = check_diagonal_winner(input_list, size)
    if winner == None:
        winner = check_diagonal_winner(list(zip(*reversed(input_list))), size)
    return winner

def transpose(input_list):
    """
    Transpose a two dimensinal list.

    Arguments:
    input_list -- a two dimensional list for transposing.
    
    Returns:
    result -- transposed two dimensinal list.
    
    """
    result = []
    for i in range(len(input_list[0])):
        new_line = [new_list[i] for new_list in input_list]
        result.append(new_line)
    return result
    
def check_row_winner(input_list, size):
    """
    Check the winner number in row direction.

    Arguments:
    input_list -- a two dimensional list for checking.
    size -- the length for winning.
    
    Returns:
    winner -- the winner player number, if no winner return None.
    
    """
    for line in input_list:
        count = 1
        for idx, value in enumerate(line):
            if line[idx] == line[idx+1]:
                count += 1
            else:
                count = 1
            if count == size and value != ' ':
                return value
            if idx == len(line)-size+1:
                break

def check_diagonal_winner(input_list, size):
    """
    Check the winner number in diagonal direction.

    Arguments:
    input_list -- a two dimensional list for checking.
    size -- the length for winning.
    
    Returns:
    winner -- the winner player number, if no winner return None.
    
    """
    for row_idx, line in enumerate(input_list):
        winner = ' '
        try:
            list_for_check = []
            for i in range(size):
                list_for_check.append(input_list[row_idx+i][i])
            if list_for_check.count(list_for_check[0]) == size:
                if list_for_check[0] != ' ':
                    return list_for_check[0] 
        except IndexError:
            winner = ' '

def draw_board_v2(input_list):
    """
    Draw game boards.

    Arguments:
    input_list -- a two dimensional list for game board.
    
    """
    h_element = ' ---'
    for v_element in input_list:
        print(h_element * len(input_list))
        row = [('| ' + j + ' ') for j in v_element]
        row = ''.join(map(str,row))
        print(row + '|')
    print(h_element * len(input_list))

def draw_turn(row, column, input_list, user):
    """
    Draw the game board after user typing a choice.

    Arguments:
    row -- the row index.
    column -- the column index.
    input_list -- a two dimensional list for game board.
    user -- the user who type the choice
    
    Returns:
    input_list -- a two dimensional list for game board after changed. If the position has been change perviously, return False.
    
    """
    mark_dict = {'player1':'X', 'player2':'O'}
    if input_list[row-1][column-1] == ' ':
        input_list[row-1][column-1] = mark_dict[user]
    else:
        print('That position has been taken, please input a new place:')
        return input_list
    return input_list
        
def require_input(user, input_list, info_dict):
    """
    Get the user's input position.

    Arguments:
    input_list -- a two dimensional list for game board.
    user -- the user who type the choice
    info_dict -- the information database.
    
    Returns:
    input_list -- a two dimensional list for game board after changed.
    
    """
    import copy
    input_list_before = copy.deepcopy(input_list)
    while True:
        row, column = input("Round {}, {}'s turn:".format(info_dict['round'], user)).split()
        input_list = draw_turn(int(row), int(column), input_list, info_dict[user])
        if input_list != input_list_before:
            break
    draw_board_v2(input_list)
    return input_list

def initiation():
    '''
    Ask user how large the game board you want
    '''
    pass

def to_the_end():
    '''
    Check is there position available.
    '''
    pass

def main():
    print('Welcome to the game!')
    user1 = input("Player 1's name:")
    user2 = input("Player 2's name:")
    info_dict = {user1:'player1', user2:'player2', 'round':1}
    input_list = [[' ',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' '],
                  [' ',' ',' ',' ',' ',' ']]
    draw_board_v2(input_list)
    while True:
        # The code is redundant, improvement needed.
        input_list = require_input(user1, input_list, info_dict)
        if check_winner(input_list, 4) not in [None, ' ']:
            print('{} win!'.format(winner))
            break
        input_list = require_input(user2, input_list, info_dict)
        if check_winner(input_list, 4) not in [None, ' ']:
            print('{} win!'.format(winner))
            break
        info_dict['round'] += 1
    
if __name__ == "__main__":
    main()

# >>> %Run test.py
# Welcome to the game!
# Player 1's name:Soi
# Player 2's name:Peruru
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# Round 1, Soi's turn:2 2
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   | X |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# Round 1, Peruru's turn:3 3
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   | X |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   | O |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# Round 2, Soi's turn:3 2
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   | X |   |   |   |   |
#  --- --- --- --- --- ---
# |   | X | O |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# Round 2, Peruru's turn:3 4
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   | X |   |   |   |   |
#  --- --- --- --- --- ---
# |   | X | O | O |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# Round 3, Soi's turn:4 2
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   | X |   |   |   |   |
#  --- --- --- --- --- ---
# |   | X | O | O |   |   |
#  --- --- --- --- --- ---
# |   | X |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# Round 3, Peruru's turn:6 6
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   | X |   |   |   |   |
#  --- --- --- --- --- ---
# |   | X | O | O |   |   |
#  --- --- --- --- --- ---
# |   | X |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   | O |
#  --- --- --- --- --- ---
# Round 4, Soi's turn:5 2
#  --- --- --- --- --- ---
# |   |   |   |   |   |   |
#  --- --- --- --- --- ---
# |   | X |   |   |   |   |
#  --- --- --- --- --- ---
# |   | X | O | O |   |   |
#  --- --- --- --- --- ---
# |   | X |   |   |   |   |
#  --- --- --- --- --- ---
# |   | X |   |   |   |   |
#  --- --- --- --- --- ---
# |   |   |   |   |   | O |
#  --- --- --- --- --- ---
# X win!
