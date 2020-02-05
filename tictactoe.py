import random

# Display the board
def display_board(board):
    print('\n' * 100)
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

# Ask whether the player like to play as 'X' or 'O'
def player_input():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 choose X or O: ').upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
# Place the marker in the desired position on the board (From position 1 to 9)
def place_marker(board, marker, position):
    board[position] = marker

# Check whether a player has won the game
def win_check(board, mark):
    # Check all rows, columns, and diagnals to see if marker matches
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # First horizontal
            (board[4] == mark and board[5] == mark and board[6] == mark) or # Second horizontal
            (board[7] == mark and board[8] == mark and board[9] == mark) or # Third horizontal
            (board[1] == mark and board[4] == mark and board[7] == mark) or # First vertical
            (board[2] == mark and board[5] == mark and board[8] == mark) or # Second vertical
            (board[3] == mark and board[6] == mark and board[9] == mark) or # Third vertical
            (board[1] == mark and board[5] == mark and board[9] == mark) or # Left diagonal
            (board[3] == mark and board[5] == mark and board[7] == mark))   # Right diagonal

# Randomly choose which player go first (Either X or O go first)
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Check if the position on the board is not filled with 'X' or 'O'
def space_check(board, position):
    return board[position] == ' '

# Check if the board is full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    
    # Board is full if return True
    return True

# Ask for the player's next position
def player_choice(board):
    position = 0
    
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Please choose your next position (1 - 9): '))
    
    return position

# Ssk if the player wants to play again
def replay():
    return input('Do you want to replay? Enter Yes or No: ').lower().startswith('y')


# Main function
#############################################################################
print('Welcom to Tic Tac Toe')

while True:
    board = [' '] * 10
    player1, player2 = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play = input('Are you ready to play? Enter Yes or No: ')

    if play.lower() == 'yes':
        gameOn = True
    else:
        gameOn = False

    while gameOn:
        # If this is player 1 turn, place player 1 marker on the desired position
        if turn == 'player1':
            display_board(board) # Show the board
            pos = player_choice(board) # Choose a position
            place_marker(board, player1, pos) # Place the marker on the position

            # Check if player 1 has won the game
            if win_check(board, player1):
                display_board(board)
                print('Player 1 has won')
                gameOn = False
            else:
                # Check if the game is tie
                if full_board_check(board):
                    display_board(board)
                    print('Game Tie')
                    break
                # If nobody wins or the game is tied, then continue with player 2's turn
                else:
                    turn = 'player2'

        # This is the same as player 1's code
        else:
            display_board(board)
            pos = player_choice(board)
            place_marker(board, player2, pos)

            if win_check(board, player2):
                display_board(board)
                print('Player 2 has won')
                gameOn = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Game Tie')
                    break
                else:
                    turn = 'player1'
    
    if not replay():
        break
###############################################################################



#########################################
# Test if the functions work
#########################################

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

# player_input()

# place_marker(test_board,'$',8)
# display_board(test_board)

# win_check(test_board,'X')

#########################################