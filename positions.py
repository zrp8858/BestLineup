from enum import Enum


class NflPositions(Enum):
    QB = "QB"
    RB = "RB"
    WR = "WR"
    TE = "TE"
    DST = "D/ST"
    K = "K"

class FantasyPositions(Enum):
    QB = NflPositions.QB.value
    RB = NflPositions.RB.value
    WR = NflPositions.WR.value
    TE = NflPositions.TE.value
    DST = NflPositions.DST.value
    K = NflPositions.K.value

    FLEX = "FLEX"
    BE = "BE"
