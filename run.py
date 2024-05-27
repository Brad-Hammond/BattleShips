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
     """)


def create_board(size):
    """
    Creates a game board of a given size.

    Parameters:
    size (int): The size of the board (size x size).

    Returns:
    list: A 2D list representing the board with all cells initialized to ".".
    """
    board = []
    for x in range(size):
        board.append(["."] * size)
    return board


def print_board_with_numbers(size):
    """
    Prints a preview of the board with row and column numbers.

    Parameters:
    size (int): The size of the board.

    Prints:
    None
    """
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


def print_board(board, size, reveal=False):
    """
    Prints the current state of the board.

    Parameters:
    board (list of list): The game board.
    size (int): The size of the board.
    reveal (bool): Whether to reveal the ships (default is False).

    Prints:
    None
    """
    print(" ", end=" ")
    for col in range(size):
        print(col, end=" ")
    print()
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


def place_ships(board, ships):
    """
Places ships on the board at random positions and orientations.

Parameters:
    board (list of str): The game board represented as a 2D list.
    ships (list of int): A list containing the lengths of ships to be placed.
                         Each integer represents the length of a ship.

Returns:
    list of tuple: A list of tuples where each tuple -
      represents the position and orientation of a ship.
        Each tuple contains (row, col, orientation, length), where:
        - row (int): The starting row of the ship.
        - col (int): The starting column of the ship.
        - orientation (str): The orientation of the ship
                           ('H' for horizontal, 'V' for vertical).
        - length (int): The length of the ship.
    """
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


def update_board(board, guess_row, guess_col, hit):
    """
    Updates the game board based on whether a guess was a hit or miss.

    Parameters:
    board (list of list): The game board.
    guess_row (int): The row guessed by the player.
    guess_col (int): The column guessed by the player.
    hit (bool): Whether the guess was a hit.

    Prints:
    None
    """
    if hit:
        board[guess_row][guess_col] = "X"
    else:
        board[guess_row][guess_col] = "M"


def get_board_size():
    """
    Prompts the player to enter the size of the board.

    Returns:
    int: The size of the board.
    """
    while True:
        try:
            size = int(input(
             "Enter the size of the board (e.g., 5 for a 5x5 board): "
            ))
            if size < 3:
                print("The minimum allowed board size is 3x3.")
            elif size > 10:
                print("The maximum allowed board size is 10x10.")
            else:
                return size
        except ValueError:
            print("Please enter a valid integer for the board size.")


def get_difficulty():
    """
    Prompts the player to choose a difficulty level.

    Returns:
    str: The chosen difficulty level ('easy', 'medium', or 'hard').
    """
    while True:
        difficulty = input("Choose difficulty level (easy, medium, hard): "
                           "").strip().lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        else:
            print("Please choose a valid difficulty level.")


def get_max_difficulty(difficulty):
    '''
    Sets the difficulty settings to the below:

    Easy = 50 turns

    Medium = 12 turns

    Hard = 10 turns

    Parameters:
    difficulty (str): The chosen difficulty level.

     Returns:
    int: The maximum number of turns.

    '''
    if difficulty == "easy":
        return 50
    elif difficulty == "medium":
        return 12
    elif difficulty == "hard":
        return 10


def show_instructions():
    '''
    Below are the instruction messages for the game, 1 through 10

    Prints:
    None

    '''
    print("\nInstructions:")
    print("1. After typing your name, you can chose a difficulty to play.")
    print("2. Easy will have 50 guesses, medium will have 12 and "
          "hard will have 10.")
    print("3. After this, you will chose your grid size, e.g 5x5 or 8x8. "
          "Please note maximum grid size is 10x10 and minumum us 3x3.")
    print("4. You will then be presented with a grid of your specified size.")
    print("5. Ships will be placed randomly on the grid, hidden from view. "
          "One ship will be 2 spaces long and another will be 3.")
    print("6. On each turn, you will guess a row and column to attack.")
    print("7. If you hit a part of a ship, it will be marked with 'X'.")
    print("8. If you miss, it will be marked with 'M'.")
    print("9. Your goal is to sink all the ships within the given turns.")
    print("10. You win if you sink all ships; you lose if you run out of "
          "turns.\n")


def get_player_name():
    """
    Prompts the player to enter their name.

    Returns:
    str: The player's name.
    """
    while True:
        player_name = input("Ahoy Captain! What's your name?").strip()
        if player_name:
            return player_name
        else:
            print("Please enter a valid name.")


def ask_for_instructions(player_name):
    """
    Asks the player if they want to see the instructions.

    Parameters:
    player_name (str): The player's name.

    Prints:
    None
    """
    while True:
        show_instr = input(f"Hello {player_name}, " +
                           f"would you like to know the instructions? "
                           "(yes/no):").strip().lower()
        if show_instr in ["yes", "no"]:
            break
        else:
            print("Please enter 'yes' or 'no'.")
    if show_instr == "yes":
        show_instructions()


def confirm_board_size(player_name, size):
    """
    Asks the player to confirm the chosen board size.

    Parameters:
    player_name (str): The player's name.
    size (int): The size of the board.

    Returns:
    bool: True if the player confirms the size, False otherwise.
    """
    while True:
        proceed = input(
            f"\n{player_name}, do you want to proceed with this board size? "
            "(yes/no): ").strip().lower()
        if proceed in ["yes", "no"]:
            return proceed == "yes"
        else:
            print("Please enter a valid response (yes or no).")


def get_player_guess(player_name, size):
    """
    Prompts the player to make a guess for row and column.

    Parameters:
    player_name (str): The player's name.
    size (int): The size of the board.

    Returns:
    tuple: A tuple containing the guessed row and column.
    """
    while True:
        try:
            guess_row = int(input(f"{player_name}, guess Row (0-{size-1}): "))
            guess_col = int(input(f"{player_name}, guess Col (0-{size-1}): "))
            if 0 <= guess_row < size and 0 <= guess_col < size:
                return guess_row, guess_col
            else:
                print("Oops, that's not even in the ocean.")
        except ValueError:
            print("Please enter valid integers for row and column.")


def check_hit_or_miss(board, ships_positions, guess_row, guess_col):
    """
    Checks if the player's guess is a hit or miss.

    Parameters:
    board (list of list): The game board.
    ships_positions (list of tuple): The positions and orientations of ships.
    guess_row (int): The row guessed by the player.
    guess_col (int): The column guessed by the player.

    Returns:
    bool: True if the guess is a hit, False otherwise.
    """
    if board[guess_row][guess_col] == "B":
        return True
    return False


def process_hit(board, ships_positions, guess_row, guess_col,
                ships_sunk, player_name):
    '''
    Processes a hit on the board and checks if a ship is sunk.

    Parameters:
    board (list of list): The game board.
    ships_positions (list of tuple): The positions and orientations of ships.
    guess_row (int): The row guessed by the player.
    guess_col (int): The column guessed by the player.
    ships_sunk (dict): A dictionary tracking the number of ships sunk.
    player_name (str): The player's name.

    Returns:
    bool: True if a ship is sunk, False otherwise.

    '''
    update_board(board, guess_row, guess_col, True)
    for position in ships_positions:
        row, col, orientation, length = position
        if (orientation == "H" and guess_row == row and
            guess_col in range(col, col + length)) or \
           (orientation == "V" and guess_col == col and
           guess_row in range(row, row + length)):
            if all(board[row + (i if orientation == "V" else 0)]
                   [col + (i if orientation == "H" else 0)] == "X"
                   for i in range(length)):
                print(f"Congratulations {player_name}, " +
                      f"you sunk a {length}-unit ship!")
                ships_sunk[length] += 1
                return True
    return False


def play_game():
    """
    Plays the Battleship game.

    This function initializes and manages the game, including player setup,
    game setup, and the main game loop.

    Steps:
    1. Get player's name.
    2. Ask if the player wants to see the instructions.
    3. Get the difficulty level from the player and set the number of turns.
    4. Get the board size from the player and confirm it.
    5. Create the game board and place the ships.
    6. Start the game loop where the player makes -
       guesses until they win or run out of turns.
    7. Print the final results of the game.

    Parameters:
    None

    Prints:
    None
    """
    # Step 1: Get player's name
    player_name = get_player_name()

    # Step 2: Ask if the player wants to see the instructions
    ask_for_instructions(player_name)

    # Step 3: Get the difficulty level from the player
    # Also, set the number of turns
    difficulty = get_difficulty()
    turns = get_max_difficulty(difficulty)

    # Step 4: Get the board size from the player and confirm it
    while True:
        size = get_board_size()
        print_board_with_numbers(size)
        if confirm_board_size(player_name, size):
            break

    # Step 5: Create the game board and place the ships
    board = create_board(size)
    ships = [2, 3]
    ships_positions = place_ships(board, ships)

    print("Let's play Battleship!")

    ships_sunk = {length: 0 for length in ships}
    total_ships_sunk = 0
    game_over = False

    # Step 6: Start the game loop
    for turn in range(turns):
        print("\nTurn", turn + 1)
        print_board(board, size)

        # Get player's guess
        guess_row, guess_col = get_player_guess(player_name, size)

        # Check if the cell has already been guessed
        if board[guess_row][guess_col] in ["X", "M"]:
            print("You guessed that one already.")
            continue

        # Check if the guess is a hit or miss
        if check_hit_or_miss(board, ships_positions, guess_row, guess_col):
            print("Congratulations! You hit a ship!")
            if process_hit(board, ships_positions, guess_row, guess_col,
                           ships_sunk, player_name):
                total_ships_sunk += 1
                remaining_ships = len(ships) - total_ships_sunk
                print(f"You have sunk {total_ships_sunk} " +
                      f"ship{'s' if total_ships_sunk > 1 else ''}. " +
                      f"{remaining_ships} " +
                      f"{'ship' if remaining_ships == 1 else 'ships'} " +
                      f"remaining.")
        else:
            print("You missed!")
            update_board(board, guess_row, guess_col, False)

        # Check if all ships are sunk
        if total_ships_sunk == len(ships):
            game_over = True
            break

    # Step 7: Print the final results of the game
    if total_ships_sunk == len(ships):
        print("\nCongratulations! You sunk all the battleships!")
    else:
        print("\nGame Over. You ran out of turns.")
    print("The final board was:")
    print_board(board, size, reveal=True)


play_game()
