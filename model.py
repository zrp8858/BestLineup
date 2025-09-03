from typing import List
from player import Player
from positions import FantasyPositions, NflPositions


class Model:
    def __init__(self) -> None:
        # Initialize empty list of players
        self.players: List[Player] = []

        # Lineup points
        self.starterPts = 0.0
        self.totalPts = 0.0

    # Lineup Getters
    # Point Getters
    def getStarters(self) -> List[Player]:
        return [player for player in self.players if player.pos != FantasyPositions.BE]

    def getFullLineup(self) -> List[Player]:
        return self.players
    
    # Sorting Getters
    def getQbs(self) -> List[Player]:
        return [player for player in self.players if player.nflPos == NflPositions.QB]
    
    def getRbs(self) -> List[Player]:
        return [player for player in self.players if player.nflPos == NflPositions.RB]
    
    def getWrs(self) -> List[Player]:
        return [player for player in self.players if player.nflPos == NflPositions.WR]
    
    def getTes(self) -> List[Player]:
        return [player for player in self.players if player.nflPos == NflPositions.TE]
    
    def getDsts(self) -> List[Player]:
        return [player for player in self.players if player.nflPos == NflPositions.DST]
    
    def getKs(self) -> List[Player]:
        return [player for player in self.players if player.nflPos == NflPositions.K]

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
