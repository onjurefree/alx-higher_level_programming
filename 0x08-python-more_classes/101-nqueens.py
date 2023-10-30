#!/usr/bin/python3
"""
This class solves the N-queen puzzle challenge
function is_safe - In this function we are checking if its safe
to place queen at a specific position. "row, col" on the board
"""

from sys import argv


def is_safe(board, row, col):

    for i in range(row):
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True


def nqueen_game(n):

    def util(board, row):
        if row == n:
            print([[i, board[i]] for i in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                util(board, row + 1)
                board[row] = -1

    if not str(n).isdigit():
        print("N must be a number")
        exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [-1] * n
    util(board, 0)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    nqueen_game(argv[1])
