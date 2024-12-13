def create_game() -> dict:
    return {
        'board': [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ],  # could be better board[1, 1]
        'turn': 'X',
        'counter': 0,
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


def start_again():
    return int(input("do you want a 1 - rematch / 2 - new game/ 3 - end game "))



def play_x_o():
    overall_scores = {'X': 0, 'O': 0}

    while True:
        scores = {'X': 0, 'O': 0}  # Reset scores for a new game if not a rematch
        rematch = False

        while True:
            # prepare_game
            my_game = create_game()
            # prepare_board ?

            # while board_is_not_full and there_is_no_win:
            while True:
                #   X player, play
                #   input location - valid: 1. range 1-3/1-3 2. free cell
                draw_board(my_game)
                player = input_square(my_game, my_game['turn'])
                while player == -1:
                    player = input_square(my_game, my_game['turn'])
                my_game['counter'] += 1
                #   check if won ?
                if check_win(my_game, my_game['turn']):
                    scores[my_game['turn']] += 1
                    overall_scores[my_game['turn']] += 1
                    draw_board(my_game)
                    break

                #   board is full (counter == 9), tie
                if check_tie(my_game):
                    draw_board(my_game)
                    print(" it's a tie")
                    break

                my_game['turn'] = 'O' if my_game['turn'] == 'X' else 'X'

            print(f"Current Match Scores: X = {scores['X']}, O = {scores['O']}")
            
            choice = input("Do you want a rematch? (yes/no): ").strip().lower()
            if choice != 'yes':
                rematch = False
                break
            rematch = True

        if not rematch:
            print("Overall Scores:")
            print(f"X = {overall_scores['X']}, O = {overall_scores['O']}")
            choice = input("Do you want to start a new game? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("Thank you for playing!")
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
