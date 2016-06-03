"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """

    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._mancala = [0]

    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        # invert the board -> store is on the first
        self._mancala = list(configuration)[::-1]

    def __str__(self):
        """
        Return string representation for Mancala board
        """
        mancala = self._mancala[::-1]

        return str(mancala)

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._mancala[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        result = False

        for value in enumerate(self._mancala):
            if value[0] == 0:
                result = value[1] > 0
            else:
                result = value[1] == 0

            if result is False:
                break

        return result

    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if self.is_outside_range(house_num):
            return False

        house_seeds = self._mancala[house_num]

        return house_num - house_seeds == 0

    def is_outside_range(self, house_num):
        return house_num > len(self._mancala) or house_num < 0

    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_outside_range(house_num):
            return

        for idx in range(0, house_num + 1):
            if idx == house_num:
                self._mancala[idx] = 0
            else:
                self._mancala[idx] = self._mancala[idx] + 1

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        shortest_legal_house = 0

        for i in range(1, 7):
            if self.is_legal_move(i):
                shortest_legal_house = i
                break

        return shortest_legal_house

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic:
        After each move, move the seeds in the house closest to the store
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """

        # backup the current configuration (new list copy)
        # 1. get the next legal house with: choose_move
        # 2. store the move in a list
        # 3. move the seed with: apply_move
        # Repeat
        #
        mancala_backup = self._mancala[:]
        mancala_moves = []

        next_house = self.choose_move()

        while self.is_legal_move(next_house):

            mancala_moves.append(next_house)

            self.apply_move(next_house)

            next_house = self.choose_move()


        self._mancala = mancala_backup[:]

        return mancala_moves


# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """

    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"

    config1 = [6, 4, 2, 3, 1, 0, 0]
    my_game.set_board(config1)

    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[6 - 1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[6 - 3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[6 - 5]

    my_game.set_board([6, 4, 2, 3, 1, 1, 0])
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(6), "Expected:", True
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(5), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(4), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(3), "Expected:", True
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(2), "Expected:", False
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(1), "Expected:", True
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(20), "Expected:", False

    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([6, 4, 2, 3, 1, 0, 1])

    my_game.apply_move(3)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([6, 4, 2, 0, 2, 1, 2])

    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([6, 4, 2, 0, 2, 0, 3])

    my_game.apply_move(2)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([6, 4, 2, 0, 0, 1, 4])

    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([6, 4, 2, 0, 0, 0, 5])

    my_game.apply_move(6)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([0, 5, 3, 1, 1, 1, 6])

    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([0, 5, 3, 1, 1, 0, 7])

    my_game.apply_move(5)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([0, 0, 4, 2, 2, 1, 8])

    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([0, 0, 4, 2, 2, 0, 9])

    my_game.apply_move(2)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([0, 0, 4, 2, 0, 1, 10])

    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([0, 0, 4, 2, 0, 0, 11])

    my_game.apply_move(4)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([0, 0, 0, 3, 1, 1, 12])

    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([0, 0, 0, 3, 1, 0, 13])

    my_game.apply_move(3)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([0, 0, 0, 0, 2, 1, 14])

    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([0, 0, 0, 0, 2, 0, 15])

    my_game.apply_move(2)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str(my_game) == str([0, 0, 0, 0, 2, 1, 16])


    my_game.set_board([0, 0, 2, 1, 4, 5, 4])
    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 2

    my_game.set_board([0, 1, 2, 1, 4, 5, 4])
    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1

    my_game.set_board([0, 1, 2, 0, 0, 0, 0])
    print "Testing plan_moves - Computed:", my_game.plan_moves(), "Expected:", [1, 2, 1]

    my_game.set_board(config1)
    print "Testing plan_moves - Computed:", my_game.plan_moves(), "Expected:", [5, 1, 2, 1, 4, 1, 3, 1, 2, 1]

    my_game.set_board([0, 0, 0, 0, 0, 0, 0])
    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", False

    my_game.set_board([6, 4, 2, 3, 1, 0, 0])
    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", True

    # add more tests here

test_mancala()


# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())
