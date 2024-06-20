from enum import Enum
from collections import deque
import random

# add comments before every class defining what the methods do and
# This has examples of singleton and factory design patterns


class GameStatus(Enum):
    NOT_STARTED = 1
    STARTED = 2
    FINISHED = 3


class Dice:
    __instance = None
    __max_value: int

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Dice, cls).__new__(cls)
        return cls.__instance

    def __init__(self, max_val=6):
        self.__max_value = max_val

    def roll(self):
        return random.randint(1, self.__max_value)


class Player:
    def __init__(self, name):
        self.__name = name
        self.__position = 0

    def move(self, steps):
        self.__position += steps

    def get_position(self):
        return self.__position

    def get_name(self):
        return self.__name


class PlayerFactory:
    @staticmethod
    def create_player(name):
        return Player(name)


class Board:
    __sl_map: dict
    __size: int
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Board, cls).__new__(cls)
        return cls.__instance

    def __init__(self, siz=100):
        self.__size = siz
        self.__sl_map = {}

    def add_snake(self, start, end):
        if start < end:
            print("Failed to add cuz head lower than tail")
        elif start in self.__sl_map:
            print("Failed to add cuz position already occupied")
        else:
            self.__sl_map[start] = end
            print("Added snake from position " + str(start))

    def add_ladder(self, bottom, top):
        if bottom > top:
            print("Failed to add cuz bottom greater than top")
        elif bottom in self.__sl_map:
            print("Failed to add cuz position already occupied")
        else:
            self.__sl_map[bottom] = top
            print("Added ladder from position " + str(bottom))

    def get_position(self, pos):
        if pos in self.__sl_map:
            return self.__sl_map[pos]
        return pos

    def get_size(self):
        return self.__size


class Game:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Game, cls).__new__(cls)
        return cls.__instance

    def __init__(self, details=None):
        self.__board = Board(details.get('board', 100))
        self.__players = deque()
        self.__game_status = GameStatus.NOT_STARTED
        self.__dice = Dice(details.get('dice', 6))

        for snake in details.get('snakes', []):
            self.__board.add_snake(snake[0], snake[1])

        for ladder in details.get('ladders', []):
            self.__board.add_ladder(ladder[0], ladder[1])

    def add_player(self, player):
        self.__players.append(player)

    def start_game(self):
        if self.__game_status is GameStatus.NOT_STARTED:
            self.__game_status = GameStatus.STARTED
            self.play()

    def play(self):
        while self.__game_status is GameStatus.STARTED and len(self.__players) > 1:
            add_back = True
            curr_player = self.__players.popleft()
            dice_roll = self.__dice.roll()
            if curr_player.get_position() + dice_roll == self.__board.get_size():
                curr_player.move(dice_roll)
                add_back = False
                # the player is done
                print(f"Player {curr_player.get_name()} is done!")
                if len(self.__players) <= 1:
                    self.__game_status = GameStatus.FINISHED
            elif curr_player.get_position() + dice_roll < self.__board.get_size():
                curr_player.move(dice_roll)
            if add_back:
                self.__players.append(curr_player)


deets = {
    'board': 100,
    'dice': 6,
    'snakes': [(16, 6), (47, 26), (49, 11), (56, 53), (62, 19), (64, 60), (87, 24), (93, 73), (95, 75), (98, 78)],
    'ladders': [(1, 38), (4, 14), (9, 31), (21, 42), (28, 84), (36, 44), (51, 67), (71, 91), (80, 100)]
}
game = Game(deets)
game.add_player(PlayerFactory.create_player('Tushar'))
game.add_player(PlayerFactory.create_player('Thika'))
game.start_game()

