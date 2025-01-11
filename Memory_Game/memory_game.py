# START
import random


def init_game() -> dict[any]:
    """
    Initializes the game data structure.

    Returns:
        dict: A dictionary containing game settings, including the number of rows and columns,
              player scores, the game board, and other necessary game state information.
    """
    rows, columns = 4, 4
    cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H']

    game_data = {
        'rows': rows,
        'columns': columns,
        'score': {'player1': 0, 'player2': 0},
        'turn': 'player1',
        'game_over': False,
        'board': prepare_board(rows, columns, cards),
        'move_history': []  # all of the card flips till now
    }
    return game_data


def prepare_board(rows, columns, cards) -> dict[any]:
    """
    Prepares the game board by shuffling cards and placing them into the board structure.

    Args:
        rows (int): Number of rows in the board.
        columns (int): Number of columns in the board.
        cards (list): List of card values to be placed on the board.

    Returns:
        dict: A dictionary representing the game board, where each key is a tuple (row, col)
              and the value is a dictionary with card information (card value, flipped state, matched state).
    """
    random.shuffle(cards)
    print(cards)
    board = {}
    index = 0
    for row in range(rows):
        for col in range(columns):
            board[(row, col)] = {'card': cards[index], 'flipped': False, 'matched': False}
            index += 1
    return board
    # shuffle the cards!
    # place the cards in the board- i.e.
    # board[(0, 0)] = {'card': 'A', 'flipped': False, 'matched': False}
    # board[(0, 1)] = {'card': 'B', 'flipped': False, 'matched': False}
    # ...
    # 1, 4
    # board[(1,4)]
    # { (0, 0): {'card': 'A', 'flipped': False, 'matched': False}
    #   (0, 1): {'card': 'B', 'flipped': True, 'matched': False} ... }


def display_board(game_data):
    """
    Displays the current state of the game board, showing flipped cards and hiding others.

    Args:
        game_data (dict): The game data dictionary containing the board.
    """
    board = game_data['board']
    rows, columns = game_data['rows'], game_data['columns']
    print("  " + " ".join(str(i + 1) for i in range(columns)))
    for row in range(rows):
        line = []
        for col in range(columns):
            cell = board[(row, col)]
            if cell['flipped'] or cell['matched']:
                line.append(cell['card'])
            else:
                line.append('*')
        print(str(row + 1) + " " + " ".join(line))

def play(game_data) -> None:
    """
    Runs the main game loop, handling player turns, guessing, and score updates.

    Args:
        game_data (dict): The game data dictionary containing the board, scores, and other game information.
    """
    while True:
        if game_data['game_over']  == True:
            break
        display_board(game_data)
        current_player = game_data['turn']
        print(f"{current_player}'s turn")

        guess1 = get_valid_card(game_data)
        flip_card(game_data, guess1)
        display_board(game_data)

        guess2 = get_valid_card(game_data)
        flip_card(game_data, guess2)
        display_board(game_data)

        if check_match(game_data, guess1, guess2):
            print("Match found!")
            game_data['score'][current_player] += 1
        else:
            print("No match. Flipping back cards.")
            flip_back_cards(game_data, guess1, guess2)

        game_data['move_history'].append((guess1, guess2))
        game_data['turn'] = 'player2' if current_player == 'player1' else 'player1'

        if check_game_over(game_data):
            game_data['game_over'] = True

    print("Game over! Final scores:")
    print(game_data['score'])

def get_valid_card(game_data):
    """
    Prompts the user for a valid card position and validates the input.

    Args:
        game_data (dict): The game data dictionary containing the board.

    Returns:
        tuple: A tuple (row, col) representing the chosen card position.
    """
    while True:
        try:
            pos = input("Enter card position (row col): ").split()
            row, col = int(pos[0]) - 1, int(pos[1]) - 1
            if (row, col) in game_data['board'] and not game_data['board'][(row, col)]['flipped']:
                return (row, col)
            else:
                print("Invalid position. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Use row and column numbers.")

def flip_card(game_data, position):
    """
    Flips a card at the given position.

    Args:
        game_data (dict): The game data dictionary.
        position (tuple): A tuple (row, col) of the card to flip.
    """
    game_data['board'][position]['flipped'] = True

def flip_back_cards(game_data, pos1, pos2):
    """
    Flips back two cards if they don't match.

    Args:
        game_data (dict): The game data dictionary.
        pos1 (tuple): First card position.
        pos2 (tuple): Second card position.
    """
    game_data['board'][pos1]['flipped'] = False
    game_data['board'][pos2]['flipped'] = False

def check_match(game_data, pos1, pos2) -> bool:
    """
    Checks if two flipped cards match.

    Args:
        game_data (dict): The game data dictionary.
        pos1 (tuple): First card position.
        pos2 (tuple): Second card position.

    Returns:
        bool: True if the cards match, False otherwise.
    """
    return game_data['board'][pos1]['card'] == game_data['board'][pos2]['card']

def check_game_over(game_data) -> bool:
    """
    Checks if the game is over (all cards matched).

    Args:
        game_data (dict): The game data dictionary.

    Returns:
        bool: True if the game is over, False otherwise.
    """
    return all(cell['matched'] for cell in game_data['board'].values())

"""        
  1 2 3 4
1 * * * A
2 * * * A
3 * * * B
4 * * * B
Player 1, play: 2 2
  1 2 3 4
1 * * * A
2 * C * A
3 * * * B
4 * * * B
Player 1, play: 2 3
  1 2 3 4
1 * * * A
2 * C D A
3 * * * B
4 * * * B
Player 2, play: 
  1 2 3 4
1 * * * A
2 * * * A
3 * * * B
4 * * * B
"""
# END
