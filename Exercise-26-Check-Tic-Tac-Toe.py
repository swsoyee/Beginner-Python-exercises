'''
Exercise 26: Check Tic Tac Toe

This exercise is Part 2 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 1, Part 3, and Part 4.

As you may have guessed, we are trying to build up to a full
tic-tac-toe board. However, this is significantly more than half
an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON
a game of Tic Tac Toe, not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like
so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their
token in that space, and a 2 means that player 2 put their token
in that space.

Your task this week: given a 3 by 3 list of lists that represents
a Tic Tac Toe game board, tell me whether anyone has won, and tell
me which player won, if any. A Tic Tac Toe win is 3 in a row -
either in a row, a column, or a diagonal. Don’t worry about the
case where TWO people have won - assume that in every board there
will only be one winner.

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
    
        
def main():
    #draw_board(int(input('Please input the size of board:')))
    winner_is_2 = [[2, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]

    winner_is_1 = [[1, 2, 0],
                   [2, 1, 0],
                   [2, 1, 1]]

    winner_is_also_1 = [[0, 1, 0],
                        [2, 1, 0],
                        [2, 1, 1]]

    no_winner = [[1, 2, 0],
                 [2, 1, 0],
                 [2, 1, 2]]

    also_no_winner = [[1, 2, 0],
                      [2, 1, 0],
                      [2, 1, 0]]
    
    also_no_winner1 = [[2, 1, 0, 1],
                      [2, 1, 0, 2],
                      [1, 0, 0, 1],
                      [2, 1, 0, 2]]
    
    winner_is_2 = [[2, 1, 0, 0],
                   [2, 1, 0, 2],
                   [1, 0, 2, 1],
                   [2, 2, 0, 2]]
    
    print(check_winner(winner_is_2, 3))
    print(check_winner(winner_is_1, 3))
    print(check_winner(winner_is_also_1, 3))
    print(check_winner(no_winner, 3))
    print(check_winner(also_no_winner, 3))
    print(check_winner(also_no_winner1, 3))
    print(check_winner(winner_is_2, 3))
    
if __name__ == "__main__":
    main()

# Test Part
# >>> %Run test.py
# 2
# 1
# 1
# None
# None
# None
# 2
