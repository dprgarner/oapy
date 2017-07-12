from client import GomokuBase


class Gomoku(GomokuBase):
    """
    Write your bot here!
    """

    def play_turn(self, state, player):
        """
        Given the state (a list of 15*15 spaces, each -1s, 0s, and 1s) and the
        player number -1 for black, 1 for white), return the index of the place
        to play (from 0 to 15*15 - 1).
        """
        return sum(abs(i) for i in state)


Gomoku()
