import random

class IncidenceCube:
    def __init__(self, size):
        self.size = size
        self.cube = [[[0 for k in range(size)] for j in range(size)] for i in range(size)]

        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    self.cube[i][j][(i + j) % self.size] = 1

    def __str__(self):
        s = ''
        for x in self.cube:
            for y in x:
                for z in y:
                    s += str(z)
                s += ' '
            s += '\n'
        return s

    def toSquare(self):
        s = ''
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    if self.cube[i][j][k] == 1:
                        s += str(k)+' '
                        break
            s += '\n'
        return s

    def shuffle(self):
        # for i in range(self.size * self.size * self.size):
        for i in range(self.size*self.size*self.size):
            # Assume we have a "proper" matrix...
            #
            # Pick a random zero from the incidence cube...

            rx = random.randrange(0, self.size)
            ry = random.randrange(0, self.size)
            rz = random.randrange(0, self.size)
            while self.cube[rx][ry][rz] == 1:
                rx = random.randrange(0, self.size)
                ry = random.randrange(0, self.size)
                rz = random.randrange(0, self.size)

            ox = 0
            oy = 0
            oz = 0

            for j in range(self.size):
                if self.cube[j][ry][rz] == 1:
                    ox = j
                if self.cube[rx][j][rz] == 1:
                    oy = j
                if self.cube[rx][ry][j] == 1:
                    oz = j

            # do the +/- 1 move...
            # These are all square with zeros in them...
            self.cube[rx][ry][rz] += 1
            self.cube[rx][oy][oz] += 1
            self.cube[ox][ry][oz] += 1
            self.cube[ox][oy][rz] += 1

            # These all have ones, except for maybe the last one...
            self.cube[rx][ry][oz] -= 1
            self.cube[rx][oy][rz] -= 1
            self.cube[ox][ry][rz] -= 1
            self.cube[ox][oy][oz] -= 1

            while self.cube[ox][oy][oz] < 0:
                rx = ox
                ry = oy
                rz = oz

                if bool(random.getrandbits(1)):
                    for j in range(self.size):
                        if self.cube[j][ry][rz] == 1:
                            ox = j
                else:
                    for j in range(self.size-1, -1,-1):
                        if self.cube[j][ry][rz] == 1:
                            ox = j

                if bool(random.getrandbits(1)):
                    for j in range(self.size):
                        if self.cube[rx][j][rz] == 1:
                            oy = j
                else:
                    for j in range(self.size-1, -1,-1):
                        if self.cube[rx][j][rz] == 1:
                            oy = j

                if bool(random.getrandbits(1)):
                    for j in range(self.size):
                        if self.cube[rx][ry][j] == 1:
                            oz = j
                else:
                    for j in range(self.size-1, -1,-1):
                        if self.cube[rx][ry][j] == 1:
                            oz = j

                # do the +/- 1 move...
                # These are all square with zeros in them...
                self.cube[rx][ry][rz] += 1
                self.cube[rx][oy][oz] += 1
                self.cube[ox][ry][oz] += 1
                self.cube[ox][oy][rz] += 1

                # These all have ones, except for maybe the last one...
                self.cube[rx][ry][oz] -= 1
                self.cube[rx][oy][rz] -= 1
                self.cube[ox][ry][rz] -= 1
                self.cube[ox][oy][oz] -= 1



def make_sudoku(size):
    if 0 >= size or size > 42:
        return

    cube = IncidenceCube(3)
    # print(cube)
    cube.shuffle()
    # print(cube)
    print(cube.toSquare())

    return


make_sudoku(3)
