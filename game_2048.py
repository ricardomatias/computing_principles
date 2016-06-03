"""
Clone of 2048 game.
"""

# import poc_2048_gui

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
        self.grid_height = grid_height
        self.grid_width = grid_width

        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for col in range(self.grid_width)] for row in range(self.grid_height)]

        self.matrix = {
            UP: [],
            LEFT: [],
            DOWN: [],
            RIGHT: []
        }

        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if row == 0:
                    self.matrix[UP].append((row, col))
                if row == self.grid_height - 1:
                    self.matrix[DOWN].append((row, col))
                if col == 0:
                    self.matrix[LEFT].append((row, col))
                if col == self.grid_width - 1:
                    self.matrix[RIGHT].append((row, col))

        self.new_tile()
        self.new_tile()


    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid = ''

        # replace with your code
        for row in range(self.grid_height):
            grid += str(self.grid[row]) + '\n'

        return grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        moved_tiles = 0
        initial_tiles = self.matrix[direction]
        move_offset = OFFSETS[direction]
        lines = []

        row_offset = 0
        col_offset = 0

        # UP
        # (0, 0) -> (1, 0) -> (2, 0) -> (3, 0)
        for index, value in enumerate(initial_tiles):
            if index == len(initial_tiles):
                break

            line = []

            for row, col in initial_tiles:
                line.append((row + row_offset, col + col_offset))

            lines.append(line)

            row_offset += move_offset[0]
            col_offset += move_offset[1]


        print lines



    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        row = randint(0, self.grid_height - 1)
        col = randint(0, self.grid_width - 1)
        tile = 2 if randint(0, 100) > 10 else 4

        self.grid[row][col] = tile


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        row_index = row
        col_index = col

        if self.grid_width < row_index < 0 or self.grid_width < col_index < 0:
            return

        self.grid[row_index][col_index] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        row_index = row
        col_index = col

        if self.grid_width < row_index < 0 or self.grid_width < col_index < 0:
            return

        return self.grid[row_index][col_index]


# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

def iterate_grid(grid, condition, isFilter):
    result = False

    height = len(grid) - 1
    width = len(grid[0]) - 1

    for row in range(height):
        for col in range(width):
            if isFilter:
                if condition(row, col):
                    return True
            else:
                return condition(row, col)

    return result

def test_merge():
    """
    Test code for Solitaire Mancala
    """
    game = TwentyFortyEight(5, 4)
    print 'testing < reset AND new_tile > expected:', True, 'result:', iterate_grid(game.grid, lambda row, col: game.grid[row][col] > 0, True)

    game.reset()

    game.grid[0][0] = 8
    print 'testing < get_tile > expected:', True, 'result:', game.get_tile(0, 0) == 8

    game.reset()

    game.set_tile(2, 1, 16)
    print 'testing < set_tile > expected:', True, 'result:', game.get_tile(2, 1) == 16

    game.reset()

    game.set_tile(2, 1, 16)
    print 'testing < set_tile > expected:', True, 'result:', game.get_tile(2, 1) == 16

    game.reset()

    game2 = TwentyFortyEight(4, 4)
    # filled_tiles = []
    #
    # def greather_than(row, col):
    #     if game.grid[row][col] > 0:
    #         return filled_tiles.append((row, col))
    #
    # iterate_grid(game.grid, greather_than, False)
    #
    # tile_coords = filled_tiles[0]
    # print tile_coords
    #
    # tile = game.get_tile(tile_coords[0], tile_coords[1])
    # print tile
    print game2.grid

    game2.move(LEFT)
    # print 'testing < set_tile > expected:', True, 'result:', game.get_tile(tile_coords[0], tile_coords[1]) != tile



test_merge()
