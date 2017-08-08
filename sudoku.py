import random
import time


class Board:
    def __init__(self, size):
        self.__size = size
        self.__backstep_count = 0
        self.__pointer = [0, 0]

        self.__board = []
        for rowi in range(self.__size ** 2):
            self.__board.append([])
            for columni in range(self.__size ** 2):
                # self.__board[rowi].append(((rowi//self.__size)*self.__size)+(columni//self.__size))
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

    # def generate_square(self, row, column):
    #     square_number = (((row//self.__size)*self.__size)+(column//self.__size))
    #     row_start = row//self.__size*self.__size
    #     column_start = column//self.__size *self.__size
    #
    #     success_flag = True
    #     for attempt in range(self.__size**2):
    #         success_flag = True
    #
    #         # Генерация случайных чисел для квадрата
    #         while len(self.__free_numbers[square_number]) < self.__size**2:
    #             random_number = random.randrange(1, self.__size ** 2 + 1)
    #             if random_number not in self.__free_numbers[square_number]:
    #                 self.__free_numbers[square_number].append(random_number)
    #
    #         # Очистка квадрата
    #         self.clear_square(row,column)
    #
    #         for rowi in range(row_start, row_start + self.__size):
    #             for columni in range(column_start, column_start + self.__size):
    #                 for number in self.__free_numbers[square_number]:
    #                     if self.__check_number(number,rowi, columni):
    #                         self.__board[rowi][columni] = number
    #                         self.__free_numbers[square_number].remove(number)
    #                         break
    #
    #                 if self.__board[rowi][columni] == 0:
    #                     success_flag = False
    #
    #         if success_flag:
    #             return success_flag
    #
    #     # Очистка квадрата
    #     self.clear_square(row,column)
    #     return success_flag

    def __pop_number_for_square(self, square_number):
        if len(self.__free_numbers[square_number]) > 0:
            return self.__free_numbers[square_number].pop()

    def __put_number_for_square(self, square_number, number):
        if len(self.__free_numbers[square_number]) > 0:
            self.__free_numbers[square_number].insert(0, number)

    def generate_board(self):
        rowi = 0
        while rowi < self.__size ** 2:
            columni = 0
            while columni < self.__size ** 2:
                square_number = ((rowi // self.__size) * self.__size) + (columni // self.__size)

                for attempt in range(len(self.__free_numbers[square_number])):
                    number = self.__pop_number_for_square(square_number)

                    if self.__check_number(number, rowi, columni):
                        self.__board[rowi][columni] = number
                        # columni += 1
                        break
                    else:
                        self.__put_number_for_square(square_number, number)

                if self.__board[rowi][columni] == 0:  # Шаг назад
                    self.__pointer = [rowi, columni]
                    # print(self.__pointer)
                    self.__backstep_count += 1
                    # if columni > 0:
                    #     columni -=1
                    columni += 1
                else:  # Шаг вперед
                    columni += 1

            rowi += 1

            # print(self.__backstep_count)


def make_sudoku(size):
    board = Board(size)
    board.generate_board()

    print(board)


# for size in range(1, 42):
#     start = time.time()
#     make_sudoku(size)
#     end = time.time()
#     print(size, end - start, sep=': ')
