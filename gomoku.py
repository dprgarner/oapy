from client import GomokuBase

class Gomoku(GomokuBase):
    """
    Write your bot here!
    """

    def play_turn(self, state, player):
        """
        Given the state (represented as a single list of 15*15 integers, -1 for
        the first player, 1 for the second player, 0 for empty) and the player
        number (-1 if this bot is the first player, 1 if the bot is the second
        player), return the index of the place to play (from 0 to 15*15-1).
        """
        return sum(abs(i) for i in state)


Gomoku()
