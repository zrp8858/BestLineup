class Model:
    def __init__(self):
        self.messageData = "Enter a player!"
        self.players = []

    def getMessageData(self):
        return self.messageData

    def setMessageData(self, newData):
        self.messageData = newData

    def getPlayers(self):
        return self.players

    def addPlayerData(self, player):
        self.players.append(player)
