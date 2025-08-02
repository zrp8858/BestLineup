import tkinter as tk


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Best Lineup Calculator")

        # Headers for adding a player
        self.nameLabel = tk.Label(self, text="Name")
        self.nameLabel.grid(row=0, column=0, padx=10)

        self.positionLabel = tk.Label(self, text="Position")
        self.positionLabel.grid(row=0, column=1, padx=10)

        self.pointsLabel = tk.Label(self, text="Points")
        self.pointsLabel.grid(row=0, column=2, padx=10)

        # Fields for adding a player
        self.nameEntry = tk.Entry(self)
        self.nameEntry.grid(row=1, column=0, padx=10, pady=10)

        self.positionEntry = tk.Entry(self)
        self.positionEntry.grid(row=1, column=1, padx=10, pady=10)

        self.pointsEntry = tk.Entry(self)
        self.pointsEntry.grid(row=1, column=2, padx=10, pady=10)

        self.button = tk.Button(self, text="Add Player")
        self.button.grid(row=1, column=3, padx=10, pady=10)

        self.errorLabel = tk.Label(self, text="", anchor="center", justify="center")
        self.errorLabel.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

        # Best Fantasy Lineup
        self.lineupFrame = tk.Frame(self)
        self.lineupFrame.grid(row=3, column=0, columnspan=4)

        self.qbLabel = tk.Label(self.lineupFrame, text="QB")
        self.qbLabel.grid(row=0, column=0, padx=40, pady=(25, 10))

        self.qbName = tk.Label(self.lineupFrame, text="N/A")
        self.qbName.grid(row=0, column=1, padx=40, pady=(25, 10))

        self.qbPts = tk.Label(self.lineupFrame, text="0.0")
        self.qbPts.grid(row=0, column=2, padx=40, pady=(25, 10))

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
