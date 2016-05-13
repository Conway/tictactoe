class Board:
    def __init__(self):
        # Initializes a board, creates the matrix and sets the dimension.
        self.matrix = [[None]*3 for i in range(3)]
        self.dimension = 3

    def __str__(self):
        # Stringifys the board for easy display, allows use of print()
        out = ""
        for lst in self.matrix:
            out += str(lst) + "\n"
        return out

    def as_list(self):
        # converts the Board to a list for unittests
        out = []
        for lst in self.matrix:
            for x in lst:
                out += x
        return out

    def __iter__(self):
        # creates an iterator for the board
        lst = self.as_list()
        for item in lst:
            yield item

    def __bool__(self):
        # returns True if the board has a non-None value
        for lst in self.matrix:
            for val in lst:
                if val is not None:
                    return True
        return False

    def check_opening(self, down, over):
        # returns True if a space has an opening
        if self.matrix[down][over] is not None:
            return False
        return True

    def get_all_openings(self):
        # returns a list of tuples of all open coordinates
        openings = []
        for x in range(self.dimension):
            for y in range(self.dimension):
                if not self.matrix[x][y]:
                    openings.append((x, y))
        return openings

    def __getitem__(self, location):
        # returns the item at a single-integer location. The board is numbered 0-8.
        assert(location <= (self.dimension**2))
        return self.matrix[location//self.dimension][location%self.dimension]

    def __setitem__(self, location, val):
        # sets the item at a single-integer location
        assert(location < (self.dimension**2))
        if self.check_opening(location//self.dimension, location%self.dimension) == False:
            raise ValueError('This place is already taken. To override this place, use `set_val()`')
        self.matrix[location//self.dimension][location%self.dimension] = val

    def set_val(self, down, over, val, override=False):
        # sets the value at a coordinate pair
        if not override and self.check_opening(down, over):
            self.matrix[down][over] = val
        else:
            raise ValueError('This place is already taken')

    def clear(self):
        # empties the board (sets all locations to None). mostly used for unit tests
        self.matrix = [[None]*self.dimension for i in range(self.dimension)]

    def check_win(self):
        # checks all locations within a single board for winners. if a winner is found, it returns who won. else False
        # row check
        for row in self.matrix:
            if row[0] == row[1] == row[2] and row[0] != None:
                return row[0]

        # column check
        for x in range(self.dimension):
            if self.matrix[0][x] == self.matrix[1][x] == self.matrix[2][x] and self.matrix[0][x] != None:
                return self.matrix[0][x]

        # diagonal checks
            if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] and self.matrix[0][0] != None:
                return self.matrix[0][0]
            elif self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] and self.matrix[0][2] != None:
                return self.matrix[0][2]
        # else
        return False

class Cube:
    def __init__(self):
        # initializes a 3**3 board
        self.boards = [Board(), Board(), Board()]
        self.allowed = ['x', 'o']

    def __str__(self):
        # stringifies the cube
        out = ""
        for x in range(3):
            out += "---Board {0}---\n".format(str(x))
            out += str(self.boards[x]) + "\n"
        return out

    def get_available_spaces(self):
        # returns a dict that contains all open spaces - each value is a list of tuples of spaces
        spaces = {}
        for x in range(3):
            spaces[x] = self.boards[x].get_all_openings()
        return spaces

    def check_wins(self):
        # checks for a winner on the board
        # first check the 3 board objects
        for board in self.boards:
            result = board.check_win()
            if result != False:
                return result
        else:
            # 3D vertical checks
            for x in range(9):
                if self.boards[0][x] == self.boards[1][x] == self.boards[2][x] and self.boards[0][x] != None:
                    return self.boards[0][x]

            # 3D diagonal checks (yay!)
            # straight diagonals
            for x in range(3):
                if self.boards[0][x*3 + 0] == self.boards[1][x*3 + 1] == self.boards[2][x*3 + 2] and self.boards[0][x*3 + 0] != None:
                    return self.boards[0][x*3 + 0]
                elif self.boards[0][x*3 + 2] == self.boards[1][x*3 + 1] == self.boards[2][x*3 + 0] and self.boards[0][x*3 + 2] != None:
                    return self.boards[0][x*3 + 2]
                elif self.boards[0][x] == self.boards[1][3 + x] == self.boards[2][6 + x] and self.boards[0][x] != None:
                    return self.boards[0][0][x]
                elif self.boards[0][2 + x] == self.boards[1][1 + x] == self.boards[2][x] and self.boards[0][2 + x] != None:
                    return self.boards[0][2][x]
            # diagonal diagonals
            if self.boards[0][0] == self.boards[1][4] == self.boards[2][8] and self.boards[0][0] != None:
                return self.boards[0][0][0]
            elif self.boards[0][2] == self.boards[1][4] == self.boards[2][6] and self.boards[0][2] != None:
                return self.boards[0][0][2]
            elif self.boards[0][6] == self.boards[1][4] == self.boards[2][2] and self.boards[0][6] != None:
                return self.boards[0][2][0]
            elif self.boards[0][8] == self.boards[1][4] == self.boards[2][6] and self.boards[0][8] != None:
                return self.boards[0][2][2]
        return False
# for x in range(3):
#                 if self.boards[0][x][0] == self.boards[1][x][1] == self.boards[2][x][2] and self.boards[0][x][0] != None:
#                     return self.boards[0][0][0]
#                 elif self.boards[0][x][2] == self.boards[1][x][1] == self.boards[2][x][0] and self.boards[0][x][2] != None:
#                     return self.boards[0][x][2]
#                 elif self.boards[0][0][x] == self.boards[1][1][x] == self.boards[2][2][x] and self.boards[0][0][x] != None:
#                     return self.boards[0][0][x]
#                 elif self.boards[0][2][x] == self.boards[1][1][x] == self.boards[2][0][x] and self.boards[0][2][x] != None:
#                     return self.boards[0][2][x]
#             # diagonal diagonals
#             if self.boards[0][0][0] == self.boards[1][1][1] == self.boards[2][2][2] and self.boards[0][0][0] != None:
#                 return self.boards[0][0][0]
#             elif self.boards[0][0][2] == self.boards[1][1][1] == self.boards[2][2][0] and self.boards[0][0][2] != None:
#                 return self.boards[0][0][2]
#             elif self.boards[0][2][0] == self.boards[1][1][1] == self.boards[2][0][2] and self.boards[0][2][0] != None:
#                 return self.boards[0][2][0]
#             elif self.boards[0][2][2] == self.boards[1][1][1] == self.boards[2][2][0] and self.boards[0][2][2] != None:
#                 return self.boards[0][2][2]
#         return False
    def play_move(self, board, down, over, player):
        # adds a new item to the board
        assert(player in ['x', 'o'])
        self.boards[board].set_val(down, over, player)

    def clear(self):
        # clears all boards
        for board in self.boards:
            board.clear()

class HumanGame:
    class Player:
        def __init__(self, name, piece):
            # creates an internal class to manage the player
            assert(piece in ['x', 'o'])
            self.name = name
            self.piece = piece

    def __init__(self):
        self.cube = Cube()

    def start(self):
        self.cube.clear()
        print('Welcome to 3D Tic Tac Toe!')
        p1 = HumanGame.Player(input('Player 1, what is your name? '), 'x')
        print('Hello {0}, you will be x'.format(p1.name))
        p2 = HumanGame.Player(input('Player 2, what is your name? '), 'o')
        print("Hello {0}, you will be o".format(p2.name))
        moves_remaining = 27
        run = True
        while run == True:
            p1_go = True
            print(self.cube)
            while p1_go:
                try:
                    board = int(input('{0}, please make your move. Which board? '.format(p1.name)))
                    row = int(input('Please enter the row number (0-2): '))
                    column = int(input('Please enter the column number (0-2): '))

                    try:
                        self.cube.play_move(board, row, column, p1.piece)
                        moves_remaining -= 1
                        p1_go = False
                    except ValueError:
                        print('Uh oh, looks like that spot is taken. Try again!')
                except:
                    print("Uh oh, please try that again")

            result = self.cube.check_wins()
            if result != False and result in self.cube.allowed:
                print('Congratulations, {0}, you won!'.format(result))
                run = False
                break

            if moves_remaining == 0:
                print("Cat's game!")
                run = False
                break

            p2_go = True
            print(self.cube)
            while p2_go:
                try:
                    board = int(input('{0}, please make your move. Which board? '.format(p2.name)))
                    row = int(input('Please enter the row number (0-2): '))
                    column = int(input('Please enter the column number (0-2): '))

                    try:
                        self.cube.play_move(board, row, column, p2.piece)
                        moves_remaining -= 1
                        p2_go = False
                    except ValueError:
                        print('Uh oh, looks like that spot is taken. Try again!')
                except:
                    print("Uh oh, please try that again")

            result = self.cube.check_wins()
            if result != False and result in self.cube.allowed:
                print('Congratulations, {0}, you won!'.format(result))
                run = False
                break

            if moves_remaining == 0:
                print("Cat's game!")
                run = False
                break


