from positions import FantasyPositions, NflPositions


class Player:
    def __init__(
        self, name: str, nflPos: NflPositions, pos: FantasyPositions, pts: float
    ):
        self.name: str = name
        self.nflPos: NflPositions = nflPos
        self.pos: FantasyPositions = pos
        self.pts: float = pts

    # Conversion of player to custom string type
    def __str__(self):
        return f"{self.pos.name}: {self.name} - {self.pts} pts"

    def __repr__(self):
        return self.__str__()
