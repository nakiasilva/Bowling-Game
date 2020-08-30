
from BowlingGame import BowlingGame
from Player import Player

player = Player("Nakia", BowlingGame())
player.bowlingGame.roll(4)
player.bowlingGame.roll(3)
player.bowlingGame.roll(4)
player.bowlingGame.roll(6)
player.bowlingGame.roll(10)
player.bowlingGame.roll(2)
player.bowlingGame.roll(1)
player.bowlingGame.score()
