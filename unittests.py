from tictactoe import Board, Cube
import random
import unittest

class TestCases(unittest.TestCase):
    # Tests the Board object

    def test_board(self):
        # tests all of Board's methods
        board = Board()
        lst = []
        possible_choices = ['x', 'o']
        self.assertFalse(bool(board), msg="The board should be empty")
        for x in range(9):
            num = random.randint(0, len(possible_choices)-1)
            board[x] = possible_choices[num]
            lst.append(possible_choices[num])

        for place, testitem in zip(board, lst):
            self.assertEqual(place, testitem, msg="Improper iteration or improper __getitem__")

        self.assertEqual(board.as_list(), lst, msg="Board not properly converting to list")

        self.assertTrue(bool(board), msg="The board has a value in it and should be True")

        board.clear()
        self.assertFalse(board.check_win(), msg="When the board is empty, a win should be impossible")

        idx = random.randint(0, len(possible_choices)-1)
        board[6] = board[7] = board[8] = possible_choices[idx]
        self.assertEqual(board.check_win(), possible_choices[idx], msg="This should be a win")

        board.clear()
        board[0] = board[3] = board[6] = possible_choices[idx]
        self.assertEqual(board.check_win(), possible_choices[idx], msg="This should be a win")

        board.clear()
        board[1] = board[4] = possible_choices[idx]
        self.assertFalse(board.check_win(), msg="This should not be a win")

        board.clear()
        board[0] = board[4] = board[8] = possible_choices[idx]
        self.assertEqual(board.check_win(), possible_choices[idx], msg="This should be a win")

        board.clear()
        board[2] = board[4] = board[6] = possible_choices[idx]
        self.assertEqual(board.check_win(), possible_choices[idx], msg="This should be a win")

        board.clear()
        self.assertEqual(board.get_all_openings(), [(x,y) for x in range(3) for y in range(3)], msg="This board is entirely clear = all spaces should be open.")

        board[2] = board[5] = board[8] = possible_choices[idx]
        self.assertEqual(board.get_all_openings(), [(x,y) for x in range(3) for y in range(2)], msg="The third column should be occupied")
        board.clear()

        board[1] = 'x'
        with self.assertRaises(ValueError):
            board[1] = 'o'

    def test_cube(self):
        # tests all cube methods
        cube = Cube()
        possible_choices = ['x', 'o']

        idx = random.randint(0, len(possible_choices)-1)
        self.assertFalse(cube.check_wins(),msg="The cube is empty, a win should be impossible")
        for x in range(3):
            cube.play_move(0, 0, x, possible_choices[idx]) # this plays 3 items in a row
        self.assertEqual(cube.check_wins(), possible_choices[idx])

        cube.clear()
        all_openings = [(x,y) for x in range(3) for y in range(3)]
        self.assertEqual(cube.get_available_spaces(), {0:all_openings, 1:all_openings, 2:all_openings}, msg="All spaces should be open")



if __name__ == '__main__':
    unittest.main()