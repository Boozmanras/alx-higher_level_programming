#!/usr/bin/python3
import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def print_invalid_number_and_exit():
    print("N must be a number")
    sys.exit(1)

def print_invalid_size_and_exit():
    print("N must be at least 4")
    sys.exit(1)

def is_valid_position(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, n):
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_valid_position(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_invalid_number_and_exit()

    if n < 4:
        print_invalid_size_and_exit()
    
    board = [-1] * n
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    main()
