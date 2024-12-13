def create_game() -> dict:
    return {
        'board': [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ],  # could be better board[1, 1]
        'turn': 'X',
        'counter': 0
    }


def draw_board(game):
    print("  0 1 2")
    counter = 0
    for row in game['board']:
        print(counter, ' '.join(row))
        counter += 1
    print()


def input_square(game, x_or_o):
    while True:
        try:
            place = input(f"Enter location for {x_or_o} (row and column separated by a space, e.g., '1 2'): ")
            row, colm = map(int, place.split())
            if 0 <= row < 3 and 0 <= colm < 3:
                if game['board'][row][colm] != '_':
                    print(" this place is taken choose some other place")
                    return -1
                else:
                    game['board'][row][colm] = x_or_o
                    return 1
            else:
                print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input format. Please enter two numbers separated by a space.")



def check_win(game, x_o: str) -> bool:
    for i in range(3):
        if all(cell == x_o for cell in game['board'][i]):
            return True
        if all(row[i] == x_o for row in game['board']):
            return True

    if all(game['board'][i][i] == x_o for i in range(3)):
        return True
    if all(game['board'][i][2 - i] == x_o for i in range(3)):
        return True

    return False


def check_tie(game) -> bool:
    return game['counter'] >= 9


def play_x_o():
    # prepare_game
    my_game = create_game()
    x_turn: bool = True
    # prepare_board ?

    # while board_is_not_full and there_is_no_win:
    while True:
        #   X player, play
        #   input location - valid: 1. range 1-3/1-3 2. free cell
        draw_board(my_game)
        if my_game['turn'] == 'X':
            my_game['turn'] = 'O'
            x_play = input_square(my_game, 'X')
            while x_play == -1:
                x_play = input_square(my_game, 'X')
            my_game['counter'] += 1
            #   check if won ?
            if check_win(my_game, 'X'):
                print('X has won the game')
                break
            #   board is full (counter == 9), tie
            if check_tie(my_game):
                draw_board(my_game)
                print(" it's a tie")
                break
        else:
            #   O player, play
            #   input location - valid: 1. range 1-3/1-3 2. free cell
            my_game['turn'] = 'X'
            o_play = input_square(my_game, 'O')
            while o_play == -1:
                o_play = input_square(my_game, 'O')
            my_game['counter'] += 1

            #   check if won ?
            if check_win(my_game, 'O'):
                print( 'O has won the game')
                break


# X O X
# O X O
# X O X

# X _ _
# _ O _
# _ _ _


# counter = 1
# prepare_board
# while board_is_not_full and there_is_no_win:
#   X player, play
#   input location - valid: 1. range 1-3/1-3 2. free cell
#   counter += 1
#   put X in the board
#   draw the board
#   check if won ?
#      check each row X
#      check each column X
#      check 2 diagonal X
#   board is full (counter == 9), tie
#   O player, play
#   input location - valid: 1. range 1-3/1-3 2. free cell
#   counter += 1
#   put O in the board
#   board is full (counter == 9), tie
#   draw the board
#   check if won ?
#      check each row O
#      check each column O
#      check 2 diagonal O

# X O X
# O X O
# X O X

# X _ _
# _ O _
# _ _ _

if __name__ == "__main__":
    play_x_o()
