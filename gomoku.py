from client import Client


class Gomoku(Client):

    def play_game(self, first_player):
        """
        A simple implementation of a Gomoku game-playing bot.
        It just moves in the next available space.
        """
        state = [0] * (15 * 15)
        turn_number = 0

        for turn_number in range(15 * 15):
            is_my_turn = bool(turn_number % 2) != first_player

            if is_my_turn:
                # turn = self.play_turn(state)
                turn = {'type': 'Move', 'move': turn_number}
                self.send(turn)

            update = self.recv_type('PlayerMove')
            state[update['move']] = 1 if is_my_turn else -1
            if 'winner' in update:
                return


if __name__ == '__main__':
    Gomoku()
