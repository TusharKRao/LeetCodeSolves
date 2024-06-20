import unittest

from SnakeNLadder.snakeNLadder import *


class TestGameComponents(unittest.TestCase):
    def test_singleton_dice(self):
        d1 = Dice()
        d2 = Dice()
        self.assertEqual(d1, d2)

    def test_singleton_board(self):
        b1 = Board()
        b2 = Board()
        self.assertEqual(b1, b2)

    def test_singleton_game(self):
        game1 = Game({})
        game2 = Game({})
        self.assertIs(game1, game2)

    def test_dice_roll(self):
        d1 = Dice(10)
        d2 = Dice()
        r1 = d1.roll()
        r2 = d2.roll()
        self.assertTrue(r1 in range(1, 11))
        self.assertTrue(r2 in range(1, 7))

    # test the game whether it started or not by checking game status