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
    '''
    Print column numbers
    '''
    print(" ", end=" ")
    for col in range(size):
        print(col, end=" ")
    print()
    '''
    Print board with row numbers
    '''
    for row_index, row in enumerate(board):
        print(row_index, end=" ")
        for col_index, cell in enumerate(row):
            if reveal or cell == "X" or cell == "M":
                print(cell, end=" ")
            else:
                print("." if cell == "B" else cell, end=" ")
        print()

# Place Ship Function
def place_ships(board, ships):
    for ship_length in ships:
        placed = False
        while not placed:
            '''Random Selection of Vertical or Horizontal'''
            orientation = random.choice(["H", "V"])
            '''Horizontal Selection'''
            if orientation == "H":
                row = random.randint(0, len(board) - 1)
                col = random.randint(0, len(board) - ship_length)
                if all(board[row][col + i] == "." for i in range(ship_length)):
                    for i in range(ship_length):
                        board[row][col + i] = "B"
                    placed = True
                    '''If Vertical'''      
            else:
                row = random.randint(0, len(board) - ship_length)
                col = random.randint(0, len(board) - 1)
                if all(board[row + i][col] == "." for i in range(ship_length)):
                    for i in range(ship_length):
                        board[row + i][col] = "B"
                    placed = True       

# Main game function

def play_game():
    '''
    Get Player Name
    '''
    player_name = input("Ahoy Captain! What's your name?")
    '''
    Ask if player wants to see instructions
    '''
    show_instr = input(f"Hello {player_name}, would you like to know the instructions? (yes/no):").strip().lower()
    if show_instr == "yes":
        show_instructions()
    '''
    Get game difficulty
    '''
    difficulty = get_difficulty()
    turns = get_max_turns(difficulty)
    ships_sunk = 0  
    '''
    Initialize board and place ships
    '''
    board = create_board(size)
    ships = [2, 3]  # Define ships of length 2 and 3
    place_ships(board, ships)

