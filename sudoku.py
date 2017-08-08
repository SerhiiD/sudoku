import random


class Board:
    def __init__(self, size):
        self.__size = size
        self.__backstep_count = 0
        self.__pointer = [0, 0]

        self.__board = []
        for rowi in range(self.__size ** 2):
            self.__board.append([])
            for columni in range(self.__size ** 2):
                self.__board[rowi].append(0)

        self.__free_numbers = []
        for squarei in range(self.__size ** 2):
            self.__free_numbers.append([])
            # Генерация случайных чисел для квадрата
            while len(self.__free_numbers[squarei]) < self.__size ** 2:
                random_number = random.randrange(1, self.__size ** 2 + 1)
                if random_number not in self.__free_numbers[squarei]:
                    self.__free_numbers[squarei].append(random_number)

    def __str__(self):
        s = ''
        for row in self.__board:
            for cell in row:
                s += str(cell) + '\t'
            s += '\n'
        return s

    def __check_number(self, number, row, column):
        # Проверка по горизонтали
        for i in range(len(self.__board[row])):
            if self.__board[row][i] == number:
                return False

        # Проверка по вертикали
        for i in range(len(self.__board)):
            if self.__board[i][column] == number:
                return False

        # # Проверка в квадрате
        # row_start = row//self.__size*self.__size
        # column_start = column//self.__size *self.__size
        #
        # for rowi in range(row_start, row_start + self.__size):
        #     for columni in range(column_start, column_start + self.__size):
        #         if self.__board[rowi][columni] == number:
        #             return False

        return True

    def __pop_number_for_square(self, square_number):
        if len(self.__free_numbers[square_number]) > 0:
            return self.__free_numbers[square_number].pop()

    def __put_number_for_square(self, square_number, number):
        if len(self.__free_numbers[square_number]) > 0:
            self.__free_numbers[square_number].insert(0, number)

    def __move_pointer_forward(self):
        # Последняя ячейка на доске
        if self.__pointer[0] == self.__size ** 2 - 1 and self.__pointer[1] == self.__size ** 2 - 1:
            return False

        if self.__pointer[1] < self.__size ** 2 - 1:
            # Перейти к следующей колонке
            self.__pointer[1] += 1
        else:
            # Перейти к следующей строке
            self.__pointer[0] += 1
            self.__pointer[1] = 0

        return True

    def __move_pointer_backward(self):
        # Первая ячейка на доске
        if self.__pointer[0] == 0 and self.__pointer[1] == 0:
            return False

        if self.__pointer[1] > 0:
            # Перейти к предыдущей колонке
            self.__pointer[1] -= 1
        else:
            # Перейти к предыдущей строке
            self.__pointer[0] -= 1
            self.__pointer[1] = self.__size ** 2 - 1

        return True

    def __step_forward(self):
        square_number = ((self.__pointer[0] // self.__size) * self.__size) + (self.__pointer[1] // self.__size)
        for attempt in range(len(self.__free_numbers[square_number])):
            number = self.__pop_number_for_square(square_number)

            if self.__check_number(number, self.__pointer[0], self.__pointer[1]):
                self.__board[self.__pointer[0]][self.__pointer[1]] = number
                self.__move_pointer_forward()
                return True
            else:
                self.__put_number_for_square(square_number, number)

        return False

    def __step_backward(self):
        square_number = ((self.__pointer[0] // self.__size) * self.__size) + (self.__pointer[1] // self.__size)

        self.__move_pointer_backward()
        self.__put_number_for_square(square_number, self.__board[self.__pointer[0]][self.__pointer[1]])
        self.__board[self.__pointer[0]][self.__pointer[1]] = 0

    def generate_board(self):
        while self.__pointer[0] < self.__size ** 2 and self.__pointer[1] < self.__size ** 2:
            # print(self.__pointer)
            if not self.__step_forward():
                self.__step_backward()

            print(str(self))





def make_sudoku(size):
    board = Board(size)
    board.generate_board()

    print(board)


make_sudoku(3)
# for size in range(1, 42):
#     start = time.time()
#     make_sudoku(size)
#     end = time.time()
#     print(size, end - start, sep=': ')
