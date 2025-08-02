from Player import Player


def checkNumber(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Bind button to handler
        self.view.setButtonCommand(self.updateModel)

    def updateModel(self):
        # Clearing error label on button press
        self.view.setErrorLabel(0)

        # Getting input information
        newName = self.view.getNameEntry()
        newPosition = self.view.getPositionEntry()
        newPoints = self.view.getPointsEntry()

        # Checking if points isn't a number
        if not checkNumber(newPoints):
            self.view.setErrorLabel(1)
            return

        # Creating a new player object
        newPlayer = Player(newName, newPosition, float(newPoints))

        # Adding the player to the model
        self.model.addPlayerData(newPlayer)

        # Updating the view (with the first player in the model)
        self.view.setNameLabel(self.model.getPlayers()[0].getName())
        self.view.setPositionLabel(self.model.getPlayers()[0].getPosition())
        self.view.setPointsLabel(self.model.getPlayers()[0].getPoints())
