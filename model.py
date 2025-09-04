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
        return sorted(
            [player for player in self.players if player.nflPos == NflPositions.QB],
            key=lambda p: p.pts,
            reverse=True,
        )

    def getRbs(self) -> List[Player]:
        return sorted(
            [player for player in self.players if player.nflPos == NflPositions.RB],
            key=lambda p: p.pts,
            reverse=True,
        )

    def getWrs(self) -> List[Player]:
        return sorted(
            [player for player in self.players if player.nflPos == NflPositions.WR],
            key=lambda p: p.pts,
            reverse=True,
        )

    def getTes(self) -> List[Player]:
        return sorted(
            [player for player in self.players if player.nflPos == NflPositions.TE],
            key=lambda p: p.pts,
            reverse=True,
        )
    
    def getFlexs(self) -> List[Player]:
        return sorted(
            [player for player in self.players if player.nflPos == NflPositions.RB or player.nflPos == NflPositions.WR or player.nflPos == NflPositions.TE],
            key=lambda p: p.pts,
            reverse=True,
        )

    def getDsts(self) -> List[Player]:
        return sorted(
            [player for player in self.players if player.nflPos == NflPositions.DST],
            key=lambda p: p.pts,
            reverse=True,
        )

    def getKs(self) -> List[Player]:
        return sorted(
            [player for player in self.players if player.nflPos == NflPositions.K],
            key=lambda p: p.pts,
            reverse=True,
        )

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
