def print_board(board):
    print("   |   |   ")
    print(" "+board[0]+" | "+board[1]+" | "+board[2]+" ")
    print("___|___|___")
    print("   |   |   ")
    print(" "+board[3]+" | "+board[4]+" | "+board[5]+" ")
    print("___|___|___")
    print("   |   |   ")
    print(" "+board[6]+" | "+board[7]+" | "+board[8]+" ")
    print("   |   |   ")

def check_win(board, player):
    if ((board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)):
        return True
    else:
        return False

def check_tie(board):
    for i in board:
        if i == " ":
            return False
    return True

def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["X", "O"]
    turn = 0
    game_over = False

    while not game_over:
        print_board(board)
        print("It's "+players[turn]+" turn!")
        move = input("Enter position to place "+players[turn]+": ")
        move = int(move) - 1

        if board[move] == " ":
            board[move] = players[turn]
            if check_win(board, players[turn]):
                print_board(board)
                print(players[turn]+" won the game!")
                game_over = True
            elif check_tie(board):
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                turn = (turn + 1) % 2
        else:
            print("That position is already taken! Please try again.")

play_game()
