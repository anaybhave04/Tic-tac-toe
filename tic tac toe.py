def print_board(board):
    print("\n".join(["|".join(row) for row in board]))
    print()

def check_winner(board, player):
    win_conditions = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return any(all(cell == player for cell in condition) for condition in win_conditions)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    moves = 0

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (row and column): ")
        
        try:
            row, col = map(int, move.split())
            if board[row][col] != ' ':
                print("This cell is already taken. Choose another one.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers between 0 and 2.")
            continue

        board[row][col] = current_player
        moves += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif moves == 9:
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
tic_tac_toe()