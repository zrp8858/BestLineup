class Player:
    def __init__(self, name, position, points):
        self.name = name
        self.position = position
        self.points = points

    def getName(self):
        return self.name

    def getPosition(self):
        return self.position

    def getPoints(self):
        return self.points