
from BowlingGame import BowlingGame
from Player import Player

player = Player("Nakia", BowlingGame())
player.bowlingGame.roll(10)
score = player.bowlingGame.score()



