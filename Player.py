from typing import Optional
from positions import Positions


class Player:
    def __init__(
        self, name: str = "Empty", pos: Optional[Positions] = None, pts: float = 0.0
    ):
        self.name: str = name
        self.pos: Optional[Positions] = pos
        self.pts: float = pts

    # Conversion of player to custom string type
    def __str__(self):
        return f"{self.pos.name}: {self.name} - {self.pts} pts"

    def __repr__(self):
        return self.__str__()
