from client import GomokuBase

class Gomoku(GomokuBase):
    """
    Write your bot here!
    """

    def play_turn(self, state, player):
        """
        Given the state (represented as a single list of 15*15 integers, -1 for
        black, 1 for white, 0 for empty) and the player number (-1 for black,
        1 for white), return the index of the place to play
        (from 0 to 15*15-1). Black always plays first.
        """
        return sum(abs(i) for i in state)


Gomoku()
