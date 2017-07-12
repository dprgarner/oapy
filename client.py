from os import path
import json
import hashlib
import argparse

from websocket import create_connection


class Client(object):
    def __init__(self):
        self.set_args()
        self.connect()

    def send(self, msg):
        """
        All messages to the server must be JSON-serialisable.
        """
        self.ws.send(json.dumps(msg))

    def recv(self):
        """
        All messages from the server are valid JSON.
        """
        msg = self.ws.recv()
        return (
            json.loads(msg)
            if msg
            else msg
        )

    def set_args(self):
        parser = argparse.ArgumentParser(
            description='Python Client for Aoire'
        )
        parser.add_argument(
            '--hostname',
            type=str,
            required=True,
            help='The location of the server, e.g. "localhost:3000".',
        )
        parser.add_argument(
            '--user',
            type=str,
            required=True,
            help='The bot name and owner, e.g. "BotName (by David)".',
        )
        parser.add_argument(
            '--room',
            type=str,
            required=True,
            help='Where you agree to meet with another player.',
        )
        parser.add_argument(
            '--ngames',
            type=int,
            default=5,
            help='The number of consecutive games to play.',
        )
        parser.add_argument(
            '--gametype',
            type=str,
            default='Gomoku',
            help='The type of game. Only Gomoku is currently supported.',
        )
        args = parser.parse_args()
        for k, v in args._get_kwargs():
            setattr(self, k, v)

    def recv_type(self, type_):
        """
        Assert that the correct message is received.
        """
        msg = self.recv()
        assert msg and msg['type'] == type_, msg
        return msg

    def connect(self):
        try:
            self.ws = create_connection(
                'ws://{}/game'.format(self.hostname)
            )
            print('Bot connected - waiting to start game...')
            self.send({
                'type': 'StartGame',
                'room': self.room,
                'userAgent': self.user,
                'gameType': self.gametype,
                'nGames': self.ngames,
            })
            self.index = self.recv_type('YouAre')['index']

            for i in range(self.ngames):
                self.recv_type('Started')
                print('Game {} started'.format(i))
                self.play_game((self.index + i) % 2 == 0)
        finally:
            if hasattr(self, 'ws') and self.ws.connected:
                self.ws.close()


if __name__ == '__main__':
    Client()
