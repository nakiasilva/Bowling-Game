import unittest
from BowlingGame import BowlingGame
from Player import Player

class TestBowlingGame(unittest.TestCase):

    def test_frame_score(self):
        player = Player("Test", BowlingGame())
        player.bowlingGame.roll(2)
        player.bowlingGame.roll(2)
        self.assertEqual(4,player.bowlingGame.score())
    
    def test_strike_score(self):
        player = Player("Test", BowlingGame())
        player.bowlingGame.roll(10)
        player.bowlingGame.roll(2)
        player.bowlingGame.roll(2)
        self.assertEqual(18,player.bowlingGame.score())

    def test_spare_score(self):
        player = Player("Test", BowlingGame())
        player.bowlingGame.roll(8)
        player.bowlingGame.roll(2)
        player.bowlingGame.roll(2)
        player.bowlingGame.roll(1)
        self.assertEqual(15,player.bowlingGame.score())
    
    def test_all_strike(self):
        player = Player("Test", BowlingGame())
        for i in range(10):
            player.bowlingGame.roll(10)
        self.assertEqual(300,player.bowlingGame.score())

    def test_last_frame_spare(self):
        player = Player("Test", BowlingGame())
        player.bowlingGame.roll(2)
        player.bowlingGame.roll(2)
        for i in range(8):
            player.bowlingGame.roll(2)
            player.bowlingGame.roll(2)
        player.bowlingGame.roll(6)
        player.bowlingGame.roll(4)
        player.bowlingGame.roll(2)
        self.assertEqual(48,player.bowlingGame.score())
    
    def test_last_frame_strike(self):
        player = Player("Test", BowlingGame())
        player.bowlingGame.roll(2)
        player.bowlingGame.roll(2)
        for i in range(8):
            player.bowlingGame.roll(2)
            player.bowlingGame.roll(2)
        player.bowlingGame.roll(10)
        player.bowlingGame.roll(2)
        player.bowlingGame.roll(2)
        self.assertEqual(50,player.bowlingGame.score())

    

if __name__ == '__main__':
    unittest.main()