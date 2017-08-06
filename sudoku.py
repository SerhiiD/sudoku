import random

def isNumberValid(board, number, row, column):

    for cell in board[row]:
        # print(cell)
        if cell == number:
            return False

    for i in range(len(board)):
        # print(board[i][column])
        if board[i][column] == number:
            return False

    return True

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end="\t")
        print(end="\n")


def make_sudoku(size):
    board = []
    i=0
    for row in range(size**2):
        board.append([])
        for column in range(size**2):
            board[row].append(i)
            i+=1


    for squareRow in range(0, size**2, size):
        for squareColumn in range(0,size**2, size):
            # Заполнение маленького квадрата
            freeNumbers = list(range(1,size**2+1))
            # print(freeNumbers)
            i = 0
            for row in range(squareRow, squareRow+size):
                for column in range(squareColumn, squareColumn+size):
                    board[row][column] = freeNumbers[i]
                    i+=1

    print_board(board)


make_sudoku(3)
