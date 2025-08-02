from Player import Player


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Bind button to handler
        self.view.setButtonCommand(self.updateModel)

    def updateModel(self):
        # Getting input information
        newName = self.view.getNameEntry()
        newPosition = self.view.getPositionEntry()
        newPoints = self.view.getPointsEntry()

        # Creating a new player object
        newPlayer = Player(newName, newPosition, newPoints)

        # Adding the player to the model
        self.model.addPlayerData(newPlayer)

        # Updating the view (with the first player in the model)
        self.view.setNameLabel(self.model.getPlayers()[0].getName())
        self.view.setPositionLabel(self.model.getPlayers()[0].getPosition())
        self.view.setPointsLabel(self.model.getPlayers()[0].getPoints())
