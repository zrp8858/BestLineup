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

        newPlayer = (newName, newPosition, newPoints)

        self.model.addPlayerData(newPlayer)

        self.view.setNameLabel(self.model.getPlayers()[0][0])
        self.view.setPositionLabel(self.model.getPlayers()[0][1])
        self.view.setPointsLabel(self.model.getPlayers()[0][2])
