from Player import Player


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Initialize View with model data
        # Bind button to handler
        self.view.setButtonCommand(self.updateModel)

    def updateModel(self):
        newName = self.view.getNameEntry()
        newPosition = self.view.getPositionEntry()
        newPoints = self.view.getPointsEntry()

        newPlayer = Player(newName, newPosition, newPoints)

        self.model.addPlayerData(newPlayer)

        self.view.setNameLabel(self.model.getPlayers()[0].getName())
        self.view.setPositionLabel(self.model.getPlayers()[0].getPosition())
        self.view.setPointsLabel(self.model.getPlayers()[0].getPoints())
