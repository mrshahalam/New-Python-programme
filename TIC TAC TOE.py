"""
A Two-Player Tic Tac Toe Game.
1. Displaying Board
2. Play Game
3. Handle Turn
4. Check Win
    - Check Rows
    - Check Columns
    - Check Diagonals
5. Check Tie
6. Flip Player from X to O or O to X
"""

from sys import *

# Initializing the Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_going = True

winner = None

current_player = "X"

# Function: Displaying the Board
def view_board():
    print()

    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")

    print()

# Function: Handling the Turn
def handle_turn(player):

    print(player, "'s turn.")

    position = input("Enter the position where you want to place your player (1 to 9): ")

    valid = False

    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Enter the position where you want to place your player (1 to 9): ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant select that position. Please chooswe position other than", position + 1)

    board[position] = player

    view_board()

# Function: Check Rows
def checkRows():

    # Setting up Global Variable
    global game_going

    # Check if any of the following rows have all the same value and is not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row is True, then there is a win
    if row_1 or row_2 or row_3:
        game_going = False

    # Return the Winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    # No winner
    else:
        return None

# Function: Check Columns
def checkColumns():

    # Setting up Global Variable
    global game_going

    # Check if any of the following columns have all the same value and is not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column is True, then there is a win
    if column_1 or column_2 or column_3:
        game_going = False

    # Return the Winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    # No winner
    else:
        return None

# Function: Check Diagonals
def checkDiagonals():

    # Setting up Global Variable
    global game_going

    # Check if any of the following diagonals have all the same value and is not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If any diagonal is True, then there is a win
    if diagonal_1 or diagonal_2:
        game_going = False

    # Return the Winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    # No winner
    else:
        return None


# Function: Check Win
def checkWin():

    # Setting Up Global Variable
    global winner

    # Check Rows
    row_winner = checkRows()

    # Check Columns
    column_winner = checkColumns()

    # Check Diagonals
    diagonal_winner = checkDiagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

# Function: Check Tie
def checkTie():

    # Setting up the Global Variable
    global game_going

    if "-" not in board:
        game_going = False

    return

# Function: Flipping the Player from X to O or O to X
def flip_player():

    # Setting up Global Variable
    global current_player

    # If the current player was X, change it to O
    if current_player == 'X':
        current_player = 'O'

    # If the current player was O, change it to X
    elif current_player == 'O':
        current_player = 'X'
    return

# Function: Check whether the game is over or not
def check_gameOver():
    checkWin()
    checkTie()

# Function: Play The Game
def play_game():

    # Displaying the initial board
    view_board()

    # While the game is still going
    while game_going:

        # Handle a turn
        handle_turn(current_player)

        # Check if the game has ended
        check_gameOver()

        # Flip to the other player
        flip_player()

    # Game has ended
    if winner == 'X' or winner == 'O':
        print(winner + " won.")
    elif winner == None:
        print("Game Tied.")

# Function: Main Program
def main():

    while True:

        print("-------------------------")
        print("TIC TAC TOE 2-PLAYER GAME")
        print("-------------------------")

        choice = input("1. Play A New Game\n2. Exit\nEnter Your Choice: ")

        try:
            int_choice = int(choice)

            if int_choice == 1:
                play_game()
            elif int_choice == 2:
                print("Thank you for playing TIC TAC TOE Game App")
                exit()
            else:
                print("Invalid Choice. Please enter either 1 or 2.")

        except ValueError:
            print("Sorry, Wrong Input. Please enter numbers only.")

main()
