# -*- coding: utf-8 -*-
from client import Client


class Gomoku(Client):
    SIZE = 15

    def render_state(self, state):
        """
        Return a pretty string representation of the board.
        """
        MOVES_STR = {
            -1: '▒▒',
            0: '  ',
            1: '██',
        }

        numbers = '   ' + ''.join(
            str(i) + (' ' if i < 10 else '')
            for i in range(1, self.SIZE + 1)
        )
        top = '  ╔' + ('══' * self.SIZE) + '╗'
        bottom = '  ╚' + ('══' * self.SIZE) + '╝'

        collated_string = '{}\n{}\n{}\n{}'.format(
            numbers,
            top,
            '\n'.join([
                '{}║{}║'.format(
                    (' ' if i < 9 else '') + str(i + 1),
                    ''.join([
                        MOVES_STR[state[self.SIZE * i + j]]
                        for j in range(self.SIZE)
                    ]),
                )
                for i in range(self.SIZE)
            ]),
            bottom,
        )
        return collated_string

    def play_game(self, first_player):
        """
        A simple implementation of a Gomoku game-playing bot.
        It just moves in the next available space.
        """
        state = [0] * (self.SIZE * self.SIZE)
        turn_number = 0

        try:
            for turn_number in range(self.SIZE * self.SIZE):
                is_my_turn = bool(turn_number % 2) != first_player

                if is_my_turn:
                    # turn = self.play_turn(state)
                    turn = {'type': 'Move', 'move': turn_number}
                    self.send(turn)

                update = self.recv_type('PlayerMove')
                state[update['move']] = 1 if is_my_turn else -1
                if 'winner' in update:
                    return
        finally:
            print(self.render_state(state))


if __name__ == '__main__':
    Gomoku()
