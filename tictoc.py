import random
def display_board(board):
    print('    |    |')
    print(' ', board[7], '| ' , board[8], '| ', board[9] )
    print('----|----|----')
    print(' ', board[4], '| ', board[5], '| ', board[6])
    print('----|----|----')
    print(' ', board[1], '| ', board[2], '| ', board[3])
    print('    |    |')


def player_input():
    marker=''
    while not(marker == 'X' or marker == 'O'):
        marker = input("Player 1: Do you want to X or O?").upper()

        if marker == 'X':
            return ('X' , 'O')
        else:
            return ('O' , 'X')


def place_marker(board,marker,position):
    board[position] = marker


def win_check(board , mark):
    if((board[7] == board[8] == board[9] == mark) or
      (board[4] == board[5] == board[6] == mark) or
     (board[1] == board[2] == board[3] == mark) or
     (board[7] == board[4] == board[1] == mark) or
     (board[8] == board[5] == board[2] == mark) or
     (board[9] == board[6] == board[3] == mark) or
     (board[1] == board[5] == board[9] == mark) or
     (board[7] == board[5] == board[3] == mark)):
        return True
    else:
        return False


def choose_first():
    if random.randint(0 , 1) == 1:
        return 'player1'
    else:
        return 'player2'


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    else:
        return True


def player_choice(board):
    position = " "
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int (input("choose the position: [1-9]"))
        return position


def replay():
    return input("Do you want to play again? Enter y or n: ")


print("Welcome to Tic Tac Toe")
while True:
    the_board = [" "]*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + "  Will go first! ")
    play_game = input("Are you ready to play? Enter Yes or No: ")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == "player1":
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player1 won the game! ")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Game is draw! ")
                    game_on = False
                else:
                    turn = 'player2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Player2 Won the game! ")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Game is draw! ")
                    game_on = False
                else:
                    turn = "player1"
    if not replay():
        break
