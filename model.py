from typing import List
from Player import Player
from Positions import Positions


class Model:
    def __init__(self) -> None:
        # Initialize empty list of players
        self.players: List[Player] = []

        # Lineup points
        self.starterPts = 0.0
        self.totalPts = 0.0

    # Lineup Getters
    def getStarters(self) -> List[Player]:
        return [player for player in self.players if player.pos != Positions.BE]

    def getFullLineup(self) -> List[Player]:
        return self.players

    # Generic add method to player list
    def addPlayerData(self, player: Player):
        self.players.append(player)

    # Functions to generate total starting lineup & bench inclusive points
    def calcStarters(self) -> float:
        starters = self.getStarters()
        pts: float = sum(player.pts for player in starters)
        return pts

    def calcFullLineup(self) -> float:
        fullLineup = self.getFullLineup()
        pts: float = sum(player.pts for player in fullLineup)
        return pts
