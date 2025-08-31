import Player


class Model:
    def __init__(self):
        self.messageData = "Enter a player!"
        self.players = dict()

    def getMessageData(self):
        return self.messageData

    def setMessageData(self, newData):
        self.messageData = newData

    def getPlayers(self):
        return self.players

    # Adding all player data to map
    # QB Data
    def addQbData(self, qb):
        self.players['qb'].append(qb)
    # RB1 Data
    def addRb1Data(self, rb1):
        self.players['rb1'].append(rb1)
    # RB2 Data
    def addRb2Data(self, rb2):
        self.players['rb2'].append(rb2)
    # WR1 Data
    def addWr1Data(self, wr1):
        self.players['wr1'].append(wr1)
    # WR2 Data
    def addWr2Data(self, wr2):
        self.players['wr2'].append(wr2)
    # TE Data
    def addTeData(self, te):
        self.players['te'].append(te)
    # FLEX Data
    def addFlexData(self, flex):
        self.players['flex'].append(flex)
    # D/ST Data
    def addDstData(self, dst):
        self.players['dst'].append(dst)
    # K Data
    def addKData(self, k):
        self.players['k'].append(k)

    # BE1 Data
    def addBe1Data(self, be1):
        self.players['be1'].append(be1)
    # BE2 Data
    def addBe2Data(self, be2):
        self.players['be2'].append(be2)
    # BE3 Data
    def addBe3Data(self, be3):
        self.players['be3'].append(be3)
    # BE4 Data
    def addBe4Data(self, be4):
        self.players['be4'].append(be4)
    # BE5 Data
    def addBe5Data(self, be5):
        self.players['be5'].append(be5)
    # BE6 Data
    def addBe6Data(self, be6):
        self.players['be6'].append(be6)
    # BE7 Data
    def addBe7Data(self, be7):
        self.players['be7'].append(be7)
