import math

def New_Board(board):
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")


def Winner(board, player):
    win_states = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in state) for state in win_states)


def is_terminal(board):
    return Winner(board, "X") or Winner(board, "O") or " " not in board


def utility(board):
    if Winner(board, "O"):
        return 1
    elif Winner(board, "X"):
        return -1
    return 0


def actions(board):
    return [i for i in range(9) if board[i] == " "]

def result(board, action, player):
    new_board=board.copy()
    new_board[action]=player
    return new_board


def MINIMAX_SEARCH(board):
    value, move = MAX_VALUE(board)
    return move


def MAX_VALUE(board):
    if is_terminal(board):
        return utility(board), None

    v=-float("inf")
    best_move=None

    for a in actions(board):
        new_board=result(board, a, "O")
        v2, _=MIN_VALUE(new_board)

        if v2>v:
            v=v2
            best_move=a

    return v,best_move


def MIN_VALUE(board):
    if is_terminal(board):
        return utility(board), None

    v = float("inf")
    best_move = None

    for a in actions(board):
        new_board=result(board, a, "X")
        v2, _=MAX_VALUE(new_board)

        if v2<v:
            v=v2
            best_move=a

    return v,best_move


def main():
    board = [" " for _ in range(9)]

    while True:
        New_Board(board)

        try:
            move=int(input("Enter position (1-9): ")) - 1
        except ValueError:
            print("Invalid input!")
            continue

        if move not in range(9) or board[move] != " ":
            print("Invalid move!")
            continue

        board[move]="X"

        if Winner(board,"X"):
            New_Board(board)
            print("You won!")
            break

        if is_terminal(board):
            New_Board(board)
            print("Draw!")
            break

        ai_move=MINIMAX_SEARCH(board)
        board[ai_move]="O"

        if Winner(board, "O"):
            New_Board(board)
            print("AI wins!")
            break

        if is_terminal(board):
            New_Board(board)
            print("Draw!")
            break

main()