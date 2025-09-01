from Player import Player


class Model:
    def __init__(self):
        # Initialize all player slots with empty values
        self.players = {
            "qb": "",
            "rb1": "",
            "rb2": "",
            "wr1": "",
            "wr2": "",
            "te": "",
            "flex": "",
            "dst": "",
            "k": "",
            "be1": "",
            "be2": "",
            "be3": "",
            "be4": "",
            "be5": "",
            "be6": "",
            "be7": "",
        }

    # UNUSED
    def getTeam(self):
        return self.players

    # Generic add method to player map
    def addPlayerData(self, slot: str, player: Player):
        if slot in self.players:
            self.players[slot] = player
        else:
            raise ValueError(f"Invalid slot name: {slot}")

    # Position specific player add methods
    def addQbData(self, qb: Player):
        self.addPlayerData("qb", qb)

    def addRb1Data(self, rb1: Player):
        self.addPlayerData("rb1", rb1)

    def addRb2Data(self, rb2: Player):
        self.addPlayerData("rb2", rb2)

    def addWr1Data(self, wr1: Player):
        self.addPlayerData("wr1", wr1)

    def addWr2Data(self, wr2: Player):
        self.addPlayerData("wr2", wr2)

    def addTeData(self, te: Player):
        self.addPlayerData("te", te)

    def addFlexData(self, flex: Player):
        self.addPlayerData("flex", flex)

    def addDstData(self, dst: Player):
        self.addPlayerData("dst", dst)

    def addKData(self, k: Player):
        self.addPlayerData("k", k)

    # Bench slots
    def addBe1Data(self, be1: Player):
        self.addPlayerData("be1", be1)

    def addBe2Data(self, be2: Player):
        self.addPlayerData("be2", be2)

    def addBe3Data(self, be3: Player):
        self.addPlayerData("be3", be3)

    def addBe4Data(self, be4: Player):
        self.addPlayerData("be4", be4)

    def addBe5Data(self, be5: Player):
        self.addPlayerData("be5", be5)

    def addBe6Data(self, be6: Player):
        self.addPlayerData("be6", be6)

    def addBe7Data(self, be7: Player):
        self.addPlayerData("be7", be7)
