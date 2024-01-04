#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at the given position.
    """
    # Check for queens in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check for queens in the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check for queens in the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, N):
    """
    Recursively solve the N Queens problem.
    """
    if col == N:
        print_solution(board)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens(board, col + 1, N)
            board[i][col] = 0

def print_solution(board):
    """
    Print the N Queens solution.
    """
    solution = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

def nqueens(N):
    """
    Main function to solve the N Queens problem.
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
