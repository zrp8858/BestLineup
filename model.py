from Player import Player


class Model:
    def __init__(self):
        # Initialize all player slots with empty lists
        self.players = {
            "qb": [],
            "rb1": [],
            "rb2": [],
            "wr1": [],
            "wr2": [],
            "te": [],
            "flex": [],
            "dst": [],
            "k": [],
            "be1": [],
            "be2": [],
            "be3": [],
            "be4": [],
            "be5": [],
            "be6": [],
            "be7": [],
        }

    def getPlayers(self):
        return self.players

    # Generic add method to reduce code duplication
    def _addPlayer(self, slot: str, player: Player):
        if slot in self.players:
            self.players[slot].append(player)
        else:
            raise ValueError(f"Invalid slot name: {slot}")

    # Position-specific methods
    def addQbData(self, qb: Player):
        self._addPlayer("qb", qb)

    def addRb1Data(self, rb1: Player):
        self._addPlayer("rb1", rb1)

    def addRb2Data(self, rb2: Player):
        self._addPlayer("rb2", rb2)

    def addWr1Data(self, wr1: Player):
        self._addPlayer("wr1", wr1)

    def addWr2Data(self, wr2: Player):
        self._addPlayer("wr2", wr2)

    def addTeData(self, te: Player):
        self._addPlayer("te", te)

    def addFlexData(self, flex: Player):
        self._addPlayer("flex", flex)

    def addDstData(self, dst: Player):
        self._addPlayer("dst", dst)

    def addKData(self, k: Player):
        self._addPlayer("k", k)

    # Bench slots
    def addBe1Data(self, be1: Player):
        self._addPlayer("be1", be1)

    def addBe2Data(self, be2: Player):
        self._addPlayer("be2", be2)

    def addBe3Data(self, be3: Player):
        self._addPlayer("be3", be3)

    def addBe4Data(self, be4: Player):
        self._addPlayer("be4", be4)

    def addBe5Data(self, be5: Player):
        self._addPlayer("be5", be5)

    def addBe6Data(self, be6: Player):
        self._addPlayer("be6", be6)

    def addBe7Data(self, be7: Player):
        self._addPlayer("be7", be7)
