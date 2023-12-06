import argparse

def save_board_to_csv(filename, board):
    pass

def check_board_validation(board):
    pass

def generate_board():
    # TODO: generate board
    board = {}
    return board

def main():
    parser = argparse.ArgumentParser(prog="RandomBoardGenerator", description="Random Sudoku Board Generator", epilog="python3 random_board_generator.py -n 1000 -o data/board.csv")

    parser.add_argument('-n', '--number', type=int, default=1, help="Total number of boards to generate")
    parser.add_argument('-o', '--output', default="data/board.csv", help="Output file")

    args = parser.parse_args()
    total_generates = args.number
    save_file = args.output
    print(f"{total_generates} {save_file}")
    generated = 0

    while generated <= total_generates:
        board = generate_board()
        if check_board_validation(board):
            save_board_to_csv(save_file, board)
            generated += 1

if __name__ == "__main__":
    main()
