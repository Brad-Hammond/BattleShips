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
     