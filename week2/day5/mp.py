# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

# Hint
# To do this project, you basically need to create four functions:

# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
# Note: The 4 functions above are just an example. You can implement many more helper functions or choose a completely different appoach if you want.



# Tips : Consider The Following:
# What functionality will need to accur every turn to make this program work?
# After contemplating the question above, think about splitting your code into smaller pieces (functions).
# Remember to follow the single responsibility principle! each function should do one thing and do it well!



# not sure how to create gameboard... but this visual aspect needs to be in place.  and does it need to refresh everytime or is there a way to keep it consistantly in place while the game goes on?
# data strucure of board may need to be separate than visual game board
#next i will have to figure out how to play the X or O inthe appropriate spot, though this seems pretty do able
# articulating a win seems tricky. i could list out all possible win configurations but this seems ineffecient
# 





# this whole exercise really stumped me, had to reappropriate a lot of code. but trying to learn what it all means for next time


def initialize_board():
    return[[" " for _ in range(3)] for _ in range(3)]

def display_board(game_board): #creating the GUI 
    row_template = " {} | {} | {} " #creating 1 of 2 visual entites to make board
    horizontal_line = "---|---|---" #other entity
    
    for row in range(3): #genius way to construct these 2 entites, using a loop in a way that i would never have thought of myself
        print(row_template.format(game_board[row][0], game_board[row][1], game_board[row][2])) #stacking the space dividers
        if row < 2: #inserting the line dividers after every two "space" rows?
            print(horizontal_line) #making the grid
            
def get_player_move(player): #someone takes a turn
    while True: #starting the  WHILE loop 
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) # the player is invited to place their piece
            if 1 <= move <= 9: # conditions for if they enter a valid move
                row = (move - 1) // 3 # Maps the move from (1-9) to the correct grid location, to match index
                col = (move - 1) % 3
                if game_board[row][col] == " ": # this checks to make sure the space is not taken
                    return row, col
                else: # condition if the space IS taken
                    print("That cell is already occupied. Try again.") 
            else:
                print("Invalid input. Please enter a number between 1 and 9.") # if an invalid input is made
        except ValueError:
            print("Invalid input. Please enter a number.")

    
            
def update_board(board, move, player):  # i think this function is for turns afte the first turn.  
    row = (move - 1) // 3
    col = (move - 1) % 3

    if board[row][col] == " ":
        board[row][col] = player 
        return True
    else:
        print("That cell is already occupied.  Try again.")
        return False
    
def check_win(board, player): # initializing function for a win
    pass

def check_draw(board): # initalizing function for a draw
    pass

game_board = initialize_board() # clears board 
current_player = "X" # specifies whos turn it is

print("\nWelcome to TIC TAC TOE! \n")

while True:
    display_board(game_board) # call GUI function
    move = get_player_move(current_player) # calling function to get players move
    if update_board(game_board, move, current_player): # after each players turn it checks if its a win or a draw
        if check_win(game_board, current_player):
            display_board(game_board)
            print(f"Player {current_player} wins!!")
            break
        elif check_draw(game_board):
            display_board(game_board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X" # otherwise let the other player try


def check_win(board, player): # articulates the data to define a win for the check_win function
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def check_draw(board): # defines how the check_draw function checks for a draw
    for row in board:
        if " " in row:
            return False
    return True

while True:
    game_board = initialize_board()  # Initialize a new game board
    current_player = "X"

    print("\nWelcome to TIC TAC TOE! \n")

    while True:
        display_board(game_board)
        move = get_player_move(current_player)
        if update_board(game_board, move, current_player):
            if check_win(game_board, current_player):
                display_board(game_board)
                print(f"Player {current_player} wins!!")
                break
            elif check_draw(game_board):
                display_board(game_board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        break

