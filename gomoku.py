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
                print('Sending', turn)
                self.send(turn)

            update = self.recv()
            if not update:
                print(state)
                raise Exception('ended')

            move = update['move']
            state[move] = 1 if is_my_turn else -1


if __name__ == '__main__':
    Gomoku()
