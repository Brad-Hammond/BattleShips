import random

print(r"""
      
                      __/___            
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
 ____        _   _   _        ____  _     _           
| __ )  __ _| |_| |_| | ___  / ___|| |__ (_)_ __  ___ 
|  _ \ / _` | __| __| |/ _ \ \___ \| '_ \| | '_ \/ __|
| |_) | (_| | |_| |_| |  __/  ___) | | | | | |_) \__ \
|____/ \__,_|\__|\__|_|\___| |____/|_| |_|_| .__/|___/
                                           |_|        
     """ )

# Creating board

def create_board(size):
    board = []
    for x in range(size):
        board.append(["."] * size)
    return board   

# Preview of the grid with row and column numbers

def print_board_with_numbers(size):
    print("Preview of the board:")
    print(" ", end=" ")
    for col in range(size):
        print(col, end=" ")
    print()
    for row in range(size):
        print(row, end=" ")
        for col in range(size):
            print(".", end=" ")
        print()      

# Row / column function

def print_board(board, size, reveal=False):

    # Print column numbers
    print(" ", end=" ")
    for col in range(size):
        print(col, end=" ")
    print()

    # Print board with row numbers
    for row_index, row in enumerate(board):
        print(row_index, end=" ")
        for col_index, cell in enumerate(row):
            if reveal:
                print(cell, end=" ")
            else: 
                if cell == "B":
                    print(".", end=" ")
                else:
                    print(cell, end=" ")
        print()

# Place Ship Function
def place_ships(board, ships):
    ships_positions = []
    for length in ships:
        while True:
            orientation = random.choice(["H", "V"])
            if orientation == "H":
                row = random.randint(0, len(board) - 1)
                col = random.randint(0, len(board) - length)
                if all(board[row][col + i] == "." for i in range(length)):
                    for i in range(length):
                        board[row][col + i] = "B"
                    ships_positions.append((row, col, orientation, length))
                    break
            else:
                row = random.randint(0, len(board) - length)
                col = random.randint(0, len(board) - 1)
                if all(board[row + i][col] == "." for i in range(length)):
                    for i in range(length):
                        board[row + i][col] = "B"
                    ships_positions.append((row, col, orientation, length))
                    break
    return ships_positions 

# Function for updating Board   
def update_board(board, guess_row, guess_col, hit):

    # If Hit
    if hit:
        board[guess_row][guess_col] = "X"
    # If Miss    
    else: board[guess_row][guess_col] = "M"    

# Defining board size (user choice)
def get_board_size():
    while True:
        try:
            size = int(input("Enter the size of the board (e.g., 5 for a 5x5 board): "))
            # Invalid data input
            if size <= 0:
                print("Please enter a positive number for the board size.")
                # Max board size of 10x10
            elif size > 10:
                print("The maximum allowed board size is 10x10.")
            else:
                return size    
        except ValueError:
            print("Please enter a valid integer for the board size.")     

# Difficulty 

# Chosing Difficulty

def get_difficulty():
    while True:
        difficulty = input("Choose difficulty level (easy, medium, hard): ").strip().lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        else: print("Please choose a valid difficulty level.")

# Difficulty settings (Turns)

def get_max_difficulty(difficulty):
    # Settings for easy difficulty
    if difficulty == "easy":
        return 50
    # Settings for medium difficulrt
    elif difficulty == "medium":
        return 12
    # Settings for hard difficulty
    elif difficulty == "hard":
        return 10

# Function for Instructions

def show_instructions():
    print("\nInstructions:")
    print("1. After typing your name, you can chose a difficulty to play.")
    print("2. Easy will have 50 guesses, medium will have 12 and hard will have 8.")
    print("3. After this, you will chose your grid size, e.g 5x5 or 8x8. Please note maximum grid size is 10x10.")
    print("4. You will then be presented with a grid of your specified size.")
    print("5. Ships will be placed randomly on the grid, hidden from view. 1 ship will be 2 spaces long and another will be 3. ")
    print("6. On each turn, you will guess a row and column to attack.")
    print("7. If you hit a part of a ship, it will be marked with 'X'.")
    print("8. If you miss, it will be marked with 'M'.")
    print("9. Your goal is to sink all the ships within the given turns.")
    print("10. You win if you sink all ships; you lose if you run out of turns.\n")

# Main game function

def play_game():
    # Get Player Name
    player_name = input("Ahoy Captain! What's your name?")

    #Ask if player wants to see instructions
    while True:
        show_instr = input(f"Hello {player_name}, would you like to know the instructions? (yes/no):").strip().lower()
        if show_instr in ["yes", "no"]:
            break
        else:
            print("Please enter 'yes' or 'no'.")
    if show_instr == "yes":
        show_instr()

    #Get game difficulty
    difficulty = get_difficulty()
    turns = get_max_difficulty(difficulty)

    # Chose board size
    while True:
        size = get_board_size()
        print_board_with_numbers(size)
        while True:
            proceed = input(f"\n{player_name}, do you want to proceed with this board size? (yes/no): ").strip().lower()
            if proceed in ["yes", "no"]:
                break
            else:
            # Invalid Data
                print("Please enter a valid response (yes or no).")
        if proceed == "yes":
            break        

    # Initialize board and place ships
    board = create_board(size)
    # Define ships of length 2 and 3
    ships = [2, 3]  
    ships_positions = place_ships(board, ships)

    print("Let's play Battleship!")

    # Track ships sunk
    ships_sunk = {length: 0 for length in ships}
    total_ships_sunk = 0

    # Initialize game over variable
    game_over = False

    # Game loop
    for turn in range(turns):
        # Print current turn
        print("\nTurn", turn +1)
        # Displays board
        print_board(board, size)
        # Asks user for row and column guesses
        try:
            guess_row = int(input(f"{player_name}, guess Row (0-{size-1}): "))
            guess_col = int(input(f"{player_name}, guess Col (0-{size-1}): "))
        # invalid data entry / input    
        except ValueError:
            print("Please enter valid integers for row and column.")
            continue
        # Checks for user guesses
        if guess_row < 0 or guess_row >= size or guess_col < 0 or guess_col >= size:
            print("Oops, that's not even in the ocean.")
            continue   
        elif board[guess_row][guess_col] in ["X", "M"]:
            print("You guessed that one already.")
            continue
        elif board[guess_row][guess_col] == "B":
            print("Congratulations! You hit a ship!")
            update_board(board, guess_row, guess_col, True)
            # Check if ship is sunk
            for position in ships_positions:
                row, col, orientation, length = position
                if orientation == "H":
                    if guess_row == row and guess_col in range(col, col + length):
                        if all(board[row][col + i] == "X" for i in range(length)):
                            print(f"Congratulations {player_name}, you sunk a {length}-unit ship!")
                            ships_sunk[length] += 1
                            total_ships_sunk += 1
                            remaining_ships = len(ships) - total_ships_sunk
                            print(f"You have sunk {total_ships_sunk} ship{'s' if total_ships_sunk > 1 else ''}. {remaining_ships} {'ship' if remaining_ships == 1 else 'ships'} remaining.")
                            break
                else:
                    if guess_col == col and guess_row in range(row, row + length):
                        if all(board[row + i][col] == "X" for i in range(length)):
                            print(f"Congratulations {player_name}, you sunk a {length}-unit ship!")
                            ships_sunk[length] += 1
                            total_ships_sunk += 1
                            remaining_ships = len(ships) - total_ships_sunk
                            print(f"You have sunk {total_ships_sunk} ship{'s' if total_ships_sunk > 1 else ''}. {remaining_ships} {'ship' if remaining_ships == 1 else 'ships'} remaining.")
                            break
            if total_ships_sunk == len(ships):
                game_over = True
                break
        else:
            print("You missed!")
            update_board(board, guess_row, guess_col, False) 

        # Check if game is over
        if total_ships_sunk == len(ships) or turn == turns - 1:
            game_over = True
            break

    # Game Over
    if game_over:
        print("\nCongratulations! You sunk all the battleships!")
    else:
        print("\nGame Over. You ran out of turns.")
    print("The final board was:")
    print_board(board, size, reveal=True)


# play_game function call

play_game()
            
                  


    
