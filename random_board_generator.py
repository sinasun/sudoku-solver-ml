total_generates = 1

def save_board_to_csv(filename, board):
    pass

def check_board_validation(board):
    pass

def generate_board():
    # TODO: generate board
    board = {}
    return board

def main():
    generated = 0
    while generated <= total_generates: 
        board = generate_board()
        if check_board_validation(board):
            save_board_to_csv("initial_board.csv", board)
            generated += 1

if __name__ == "__main__":
    main()
