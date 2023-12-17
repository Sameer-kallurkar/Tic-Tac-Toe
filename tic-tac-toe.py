import random
import time
from pyfiglet import Figlet

def print_board(board):
    print()
    for i, row in enumerate(board):
        print(" ", end='')
        print(" | ".join(row))
        if i < 2:
            print("---+---+---")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def minimax(board, depth, maximizing_player):
    if check_winner(board, 'O'):
        return -1
    elif check_winner(board, 'X'):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board, difficulty):
    if difficulty == 'easy':
        return random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == ' '])
    elif difficulty == 'medium':
        return random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == ' '])
    elif difficulty == 'hard':
        best_val = float('-inf')
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    move_val = minimax(board, 0, False)
                    board[i][j] = ' '

                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val

        return best_move

def play():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    f = Figlet(font='slant', width=120)
    print(f.renderText("Welcome to Tic-Tac-Toe"))

    while True:
        try:
            sec_diff = int(input("Select difficulty \n1.easy, \n2.medium, \n3.hard: "))
            if sec_diff <= 3:
                break
            else:
                print("enter a valid option")
        except (ValueError, TypeError):
            print("enter a valid option")
    
    match sec_diff:
        case 1:
            difficulty = "easy"
        case 2:
            difficulty = "medium"
        case 3:
            difficulty = "hard"

    while difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty level. Please choose again.")
        difficulty = input("Select difficulty (easy, medium, or hard): ").lower()
        
    

    while True:
        print_board(board)

        while True:
            try:
                player_row = int(input("Enter your row (1, 2, 3): "))
                player_col = int(input("Enter your column (1, 2, 3)): "))
                if player_col <=3 and player_row <= 3: 
                    break
                else:
                    print("enter a valid option")
            except (TypeError, ValueError):
                print("please select valid option")
            
        player_row = player_row-1
        player_col = player_col-1

        if board[player_row][player_col] == ' ':
            board[player_row][player_col] = 'O'
        else:
            print("Invalid move. Try again.")
            continue

        if check_winner(board, 'O'):
            print_board(board)
            f = Figlet(font='slant', width=120)
            print(f.renderText("You win! Congratulations! 🎉"))
            break

        if is_board_full(board):
            print_board(board)
            f = Figlet(font='slant', width=120)
            print(f.renderText("It's a draw!"))
            break       

        print("Computer is selecting")
        print("." , end="")
        time.sleep(0.5)
        print("." , end="")
        time.sleep(0.5)
        print(".")
        computer_row, computer_col = get_best_move(board, difficulty)
        board[computer_row][computer_col] = 'X'

        if check_winner(board, 'X'):
            print_board(board)
            f = Figlet(font='slant', width=120)
            print(f.renderText("Computer wins! Better luck next time."))
            break

        if is_board_full(board):
            print_board(board)
            f = Figlet(font='slant', width=120)
            print(f.renderText("It's a draw!"))
            break

if __name__ == "__main__":
        play()
        