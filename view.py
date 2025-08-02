import tkinter as tk


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Best Lineup Calculator")

        self.nameLabel = tk.Label(self, text="")
        self.nameLabel.pack(pady=10)

        self.positionLabel = tk.Label(self, text="")
        self.positionLabel.pack(pady=10)

        self.pointsLabel = tk.Label(self, text="")
        self.pointsLabel.pack(pady=10)

        self.nameEntry = tk.Entry(self)
        self.nameEntry.pack(pady=10)

        self.positionEntry = tk.Entry(self)
        self.positionEntry.pack(pady=10)

        self.pointsEntry = tk.Entry(self)
        self.pointsEntry.pack(pady=10)

        self.button = tk.Button(self, text="Add Player")
        self.button.pack(pady=10)

        self.errorLabel = tk.Label(self, text="")
        self.errorLabel.pack(pady=10)

    def setNameLabel(self, text):
        self.nameLabel.config(text=text)

    def setPositionLabel(self, text):
        self.positionLabel.config(text=text)

    def setPointsLabel(self, text):
        self.pointsLabel.config(text=text)

    def getNameEntry(self):
        return self.nameEntry.get()

    def getPositionEntry(self):
        return self.positionEntry.get()

    def getPointsEntry(self):
        return self.pointsEntry.get()

    def setButtonCommand(self, command):
        self.button.config(command=command)

    def setErrorLabel(self, errorCode):
        match errorCode:
            # Error code 0 - No error, clear label
            case 0:
                self.errorLabel.config(text="")
            # Error code 1 - Invalid input for points
            case 1:
                self.errorLabel.config(text="Invalid input for points!")
