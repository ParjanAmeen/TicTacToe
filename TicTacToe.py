# This is a simple game of Tic Tac Toe. A list is printed in the terminal along with the deciding
# players input. A position is taken and an X or O is then placed in that position. After a players turn
# the next player can go. The input has been protected from any invalid input.

# ---- Global variables ----
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Boolean to check if the game is still going
game_still_going = True

# Setting the winner variable
winner = None

# Setting the turn
current_player = "X"

# ---- Global variables ----


# Creating a function to display the board
def display_board():

    # Printing out the board by calling the print function
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Creating a function that will handle turns
def handle_turn(player):

    # Notify the players whose turn it is
    print(player + "'s turn")

    # Having a position catch the input when asking the user the position
    position = input("Choose a position (1-9): ")

    # Creating a variable to check and see if the play is valid
    valid = False

    while not valid:

        # Checking to see if the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position between 1 and 9: ")

        # Setting the input to be a position and subtracting one to know where in the
        # board to go
        position = int(position) - 1

        # Checking to see if the position has already been marked
        if board[position] == "-":
            valid = True

        else:
            print("Position already marked. Please choose another position")

    # Setting the position into the board
    board[position] = player

    # Displaying the board
    display_board()


# Creating a function to check the rows
def check_rows():

    # Setting global variables
    global game_still_going

    # Check to see if all three rows are equal
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If row 1, 2, or 3 set game still going to false
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Returning the winner
    if row_1:
        return board[0]

    if row_2:
        return board[3]

    if row_3:
        return board[6]

    else:
        return None


# Creating a function to check the columns
def check_columns():

    # Setting global variables
    global game_still_going

    # Check to see if all three rows are equal
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If row 1, 2, or 3 set game still going to false
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Returning the winner
    if column_1:
        return board[0]

    if column_2:
        return board[1]

    if column_3:
        return board[2]

    else:
        return None


# Creating a function to check the diagonals
def check_diagonals():

    # Setting global variables
    global game_still_going

    # Check to see if all three rows are equal
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    # If row 1, 2, or 3 set game still going to false
    if diagonals_1 or diagonals_2:
        game_still_going = False

    # Returning the winner
    if diagonals_1:
        return board[0]

    if diagonals_2:
        return board[1]

    else:
        return None


# Creating a function to check if there is a win
def check_if_win():

    # Setting up global variables
    global winner

    # Check rows
    row_winner = check_rows()

    # Check columns
    column_winner = check_columns()

    # Check diagonals
    diagonal_winner = check_diagonals()

    # Check to see if there was a row winner
    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        # No winner
        winner = None


# Creating a function to check for a tie
def check_if_tie():

    # Set the global variables
    global game_still_going

    # Check to see if the dash is not on the board
    if "-" not in board:
        game_still_going = False
        return True

    else:
        return False


# Creating a function to see if the game is over
def check_if_game_over():

    # Calling check if win
    check_if_win()

    # Calling check if tie
    check_if_tie()


# Creating a function to flip the player
def flip_player():

    # Setting global variables
    global current_player

    # If the current player is X change to O
    if current_player == "X":
        current_player = "O"

    # If the current player is O change to X
    elif current_player == "O":
        current_player = "X"


# Creating a function that runs the game
def play_game():

    # Calling display board function
    display_board()

    # Creating a loop to loop through turns until the game is over
    while game_still_going:

        # Call handle turn
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flipping the player
        flip_player()

    # The game ended
    if winner == "X" or winner == "O":
        print(winner + " won. ")

    elif winner == None:
        print("Tie")


# Calling play game to run the game
play_game()
