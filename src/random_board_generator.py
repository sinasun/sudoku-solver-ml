import argparse
from board import Board

def generate_board():
    # TODO: generate board
    board = Board()
    return board

def main():
    parser = argparse.ArgumentParser(prog="RandomBoardGenerator", description="Random Sudoku Board Generator", epilog="python3 random_board_generator.py -n 1000 -o ../data/boards.csv")

    parser.add_argument('-n', '--number', type=int, default=1, help="Total number of boards to generate")
    parser.add_argument('-o', '--output', default="../data/boards.csv", help="Output file to save generated boards")

    args = parser.parse_args()
    total_generates = args.number
    save_file = args.output
    generated = 0

    while generated <= total_generates:
        board = generate_board()
        if board.is_valid():
            board.append_to_file(save_file)
            generated += 1

if __name__ == "__main__":
    main()
