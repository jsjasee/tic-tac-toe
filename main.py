from player import Player
from board import Board

player1 = Player(number=1)
player2 = Player(number=2)
board = Board()

# Initialize the game and select a token
print("Ready for some tic tac toe? Columns are 1,2,3. Rows are A,B,C. So eg. top left of the board is A1. Bottom right of the board is C3")
token = input('Player 1, please choose a token, X or O: ').upper()
if token in ["X","O"]:
    for item in ["X","O"]:
        if item == token:
            player1.token = item
        else:
            player2.token = item

# Make a move
def make_a_move(player):
    while True:
        move = input(f"{player.name} please make your move (in the format of <letter><number> eg. A1): ").lower()

        if move in board.spaces.keys():
            for key in board.spaces:
                if move == key:
                    if board.spaces[key] == " ":
                        board.spaces[key] = player.token
                        return board.update_board()
                    else:
                        print("Slot is taken please try again.")

        else:
            print("Invalid format, please try again.")

# TODO: While there is no win or lose keep repeating the make a move until all slots are used up which means draw

while not board.win_lose():
    print(make_a_move(player1))

    if board.win_lose():
        print("Player 1 won!")
        break

    print(make_a_move(player2))

    if board.win_lose():
        print("Player 2 won!")
        break

    if " " not in board.spaces.values():
        print("It's a tie!")
        break