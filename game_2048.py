"""
Clone of 2048 game.
"""

# import poc_2048_gui
import poc_simpletest

from random import randint

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {
    UP: (1, 0),
    DOWN: (-1, 0),
    LEFT: (0, 1),
    RIGHT: (0, -1)
}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result_line = line[::]

    line_len = len(result_line)

    def in_range(idx):
        """
        checks if index is in list's range
        """
        return idx + 1 < line_len

    def sort_list(item1, item2):
        """
        sorts a list
        """
        if item2 == 0:
            return -1
        else:
            return 0

    result_line = sorted(result_line, cmp=sort_list)

    for idx in range(line_len):
        if in_range(idx) and not result_line[idx] == 0:
            if result_line[idx] == result_line[idx + 1]:
                result_line[idx] = result_line[idx] + result_line[idx + 1]
                result_line[idx + 1] = 0

    result_line = sorted(result_line, cmp=sort_list)

    return result_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width

        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for col in range(self._grid_width)] for row in range(self._grid_height)]

        self._matrix = {
            UP: [],
            LEFT: [],
            DOWN: [],
            RIGHT: []
        }

        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if row == 0:
                    self._matrix[UP].append((row, col))
                if row == self._grid_height - 1:
                    self._matrix[DOWN].append((row, col))
                if col == 0:
                    self._matrix[LEFT].append((row, col))
                if col == self._grid_width - 1:
                    self._matrix[RIGHT].append((row, col))

        self.new_tile()
        self.new_tile()


    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid = ''

        # replace with your code
        for row in range(self._grid_height):
            grid += str(self._grid[row]) + '\n'

        return grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        moved_tiles = 0
        initial_tiles = self._matrix[direction]
        move_offset = OFFSETS[direction]

        if direction == 1 or direction == 2:
            length = self._grid_height
        else:
            length = self._grid_width


        for index, indices in enumerate(initial_tiles):
            line = []
            values = []

            for num in range(length):
                col = indices[0] + move_offset[0] * num
                row = indices[1] + move_offset[1] * num

                line.append((col, row))

                values.append(self.get_tile(col, row))

            merged_values = merge(values)

            for idx, val in enumerate(values):
                if val != merged_values[idx]:
                    moved_tiles += 1

            for idx, coords in enumerate(line):
                self.set_tile(coords[0], coords[1], merged_values[idx])

        for num in range(moved_tiles):
            self.new_tile()


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        def random_row_col():
            """
            Generate a random row and col number
            """
            return [randint(0, self._grid_height - 1), randint(0, self._grid_width - 1)]

        [row, col] = random_row_col()

        tile = 2 if randint(0, 100) > 10 else 4

        while self._grid[row][col] > 0:
            [row, col] = random_row_col()

        self._grid[row][col] = tile

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        row_index = row
        col_index = col

        if self._grid_width < row_index < 0 or self._grid_width < col_index < 0:
            return

        self._grid[row_index][col_index] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        row_index = row
        col_index = col

        if self._grid_width < row_index < 0 or self._grid_width < col_index < 0:
            return

        return self._grid[row_index][col_index]


def iterate_grid(grid, condition):
    result = []

    height = len(grid)
    width = len(grid[0])
    print height, width
    for row in range(height):
        for col in range(width):
            if condition(row, col): result.append(True)

    return result


def run_suite():
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    game = TwentyFortyEight(5, 4)

    suite.run_test(iterate_grid(game._grid, lambda row, col: game._grid[row][col] > 0), [True, True], "should create grid")

    game.reset()

    game.set_tile(0, 0, 8)
    suite.run_test(game.get_tile(0, 0) == 8, True, "should set/get tile with 8")

    game.reset()

    game.set_tile(2, 1, 16)
    suite.run_test(game.get_tile(2, 1) == 16, True, "should set/get tile with 16")

    game.reset()

    game.set_tile(0, 0, 8)
    game.set_tile(1, 0, 8)
    game.set_tile(2, 0, 0)
    game.set_tile(3, 0, 0)

    game.move(UP)
    suite.run_test(game.get_tile(0, 0) == 16, True, "should get tile with 16 after moving UP")

    game2 = TwentyFortyEight(4, 4)

    game2.set_tile(0, 0, 2)
    game2.set_tile(0, 1, 0)
    game2.set_tile(0, 2, 0)
    game2.set_tile(0, 3, 0)
    game2.set_tile(1, 0, 0)
    game2.set_tile(1, 1, 2)
    game2.set_tile(1, 2, 0)
    game2.set_tile(1, 3, 0)
    game2.set_tile(2, 0, 0)
    game2.set_tile(2, 1, 0)
    game2.set_tile(2, 2, 2)
    game2.set_tile(2, 3, 0)
    game2.set_tile(3, 0, 0)
    game2.set_tile(3, 1, 0)
    game2.set_tile(3, 2, 0)
    game2.set_tile(3, 3, 2)

    game2.move(UP)
    print str(game2)

    suite.report_results()



run_suite()
