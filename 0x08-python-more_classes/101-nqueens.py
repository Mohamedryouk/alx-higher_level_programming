#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if a queen can be placed in this position
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solution(board):
    # Print the current solution
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)

def solve_nqueens(board, row, N):
    # Recursive function to solve N Queens problem
    if row == N:
        # All queens are placed, print the solution
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen and move to the next row
            board[row] = col
            solve_nqueens(board, row + 1, N)
            # Backtrack if needed
            board[row] = -1

def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
