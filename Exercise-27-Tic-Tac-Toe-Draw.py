'''
Exercise 27: Tic Tac Toe Draw

In a previous exercise we explored the idea of using a list of lists
as a “data structure” to store information about a tic tac toe game.
In a tic tac toe game, the “game server” needs to know where the Xs
and Os are in the board, to know whether player 1 or player 2 (or
whoever is X and O won).

There has also been an exercise about drawing the actual tic tac toe
gameboard using text characters.

The next logical step is to deal with handling user input. When a
player (say player 1, who is X) wants to place an X on the screen,
they can’t just click on a terminal. So we are going to approximate
this clicking simply by asking the user for a coordinate of where
they want to place their piece.

As a reminder, our tic tac toe game is really a list of lists. The
game starts out with an empty game board like this:

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
The computer asks Player 1 (X) what their move is (in the format row,
col), and say they type 1,3. Then the game would print out

game = [[0, 0, X],
	[0, 0, 0],
	[0, 0, 0]]
And ask Player 2 for their move, printing an O in that place.

Things to note:

For this exercise, assume that player 1 (the first player to move) will
always be X and player 2 (the second player) will always be O.
Notice how in the example I gave coordinates for where I want to move
starting from (1, 1) instead of (0, 0). To people who don’t program,
starting to count at 0 is a strange concept, so it is better for the
user experience if the row counts and column counts start at 1. This is
not required, but whichever way you choose to implement this, it should
be explained to the player.
Ask the user to enter coordinates in the form “row,col” - a number, then
a comma, then a number. Then you can use your Python skills to figure out
which row and column they want their piece to be in.
Don’t worry about checking whether someone won the game, but if a player
tries to put a piece in a game position where there already is another
piece, do not allow the piece to go there.

Bonus:
For the “standard” exercise, don’t worry about “ending” the game - no
need to keep track of how many squares are full. In a bonus version, keep
track of how many squares are full and automatically stop asking for
moves when there are no more valid moves.

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
            if count == size and value != 0:
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
        winner = 0
        try:
            list_for_check = []
            for i in range(size):
                list_for_check.append(input_list[row_idx+i][i])
            if list_for_check.count(list_for_check[0]) == size:
                if list_for_check[0] != 0:
                    return list_for_check[0] 
        except IndexError:
            winner = 0

def draw_board(size):
    """
    Draw game boards in size of 'size'.

    Arguments:
    size -- the size of the board.
    
    """
    h_element = ' ---'
    v_element = '|   '
    for i in range(size):
        print(h_element * (size))
        print(v_element * (size+1))
    print(h_element * (size))

def draw_turn(row, column, input_list, user):
    """
    Draw the game board after user typing a choice.

    Arguments:
    row -- the row index.
    column -- the column index.
    input_list -- a two dimensional list for game board.
    user -- the user who type the choice
    
    Returns:
    input_list -- a two dimensional list for game board after changed.
    
    """
    mark_dict = {'player1':'X', 'player2':'O'}
    input_list[row-1][column-1] = mark_dict[user]
    return input_list
        
def main():
    print('Welcome to the game!')
    user1 = input("Player 1's name:")
    user2 = input("Player 2's name:")
    info_dict = {user1:'player1', user2:'player2', 'round':1}
    input_list = [['0','0','0'],['0','0','0'],['0','0','0']]
    while True:
        row, column = input("Round {}, {}'s turn:".format(info_dict['round'], user1)).split()
        input_list = draw_turn(int(row), int(column), input_list, info_dict[user1])
        print(input_list)
        row, column = input("Round {}, {}'s turn:".format(info_dict['round'], user2)).split()
        input_list = draw_turn(int(row), int(column), input_list, info_dict[user2])
        print(input_list)
        info_dict['round'] += 1
    
if __name__ == "__main__":
    main()
