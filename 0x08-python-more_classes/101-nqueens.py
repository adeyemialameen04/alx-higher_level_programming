#!/usr/bin/python3
"""N queens module"""
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]

    Args:
        board (list): The chessboard with queens placed.
        row (int): The row index to check.
        col (int): The column index to check.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n, solutions):
    """
    Recursive function to solve the N Queens problem.

    Args:
        board (list): The chessboard with queens placed.
        col (int): The current column index.
        n (int): The size of the chessboard.
        solutions (list): List to store solutions.

    Returns:
        None
    """
    # Base case: If all queens are placed, add the solution to the list
    if col == n:
        solution = []
        for row in range(n):
            for col in range(n):
                if board[row][col] == 1:
                    solution.append([row, col])
        solutions.append(solution)
        return

    # Place this queen in all safe positions
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            # Move to the next column
            solve_nqueens(board, col + 1, n, solutions)

            # If the queen cannot be placed, backtrack and remove the queen
            board[row][col] = 0


def nqueens(n):
    """
    Function to solve the N Queens problem.

    Args:
        n (int): The size of the chessboard.

    Returns:
        None
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = nqueens(n)
    for solution in solutions:
        print(solution)

# import sys
#
#
# argc = len(sys.argv)
# if argc != 2:
#     print("Usage: nqueens N")
#     sys.exit(1)
#
# n = sys.argv[1]
# if not isinstance(n, int):
#     print("N must be a number")
#     sys.exit(1)
#
# if n < 4:
#     print("N must be at least 4")
#     sys.exit(1)
