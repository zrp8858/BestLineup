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
        # QB Row
        self.qbLabel = tk.Label(self.lineupFrame, text="QB")
        self.qbLabel.grid(row=0, column=0, padx=40, pady=5)

        self.qbName = tk.Label(self.lineupFrame, text="Empty")
        self.qbName.grid(row=0, column=1, padx=40, pady=5)

        self.qbPts = tk.Label(self.lineupFrame, text="0.0")
        self.qbPts.grid(row=0, column=2, padx=40, pady=5)
        # RB1 Row
        self.rb1Label = tk.Label(self.lineupFrame, text="RB")
        self.rb1Label.grid(row=1, column=0, padx=40, pady=5)

        self.rb1Name = tk.Label(self.lineupFrame, text="Empty")
        self.rb1Name.grid(row=1, column=1, padx=40, pady=5)

        self.rb1Pts = tk.Label(self.lineupFrame, text="0.0")
        self.rb1Pts.grid(row=1, column=2, padx=40, pady=5)
        # RB2 Row
        self.rb2Label = tk.Label(self.lineupFrame, text="RB")
        self.rb2Label.grid(row=2, column=0, padx=40, pady=5)

        self.rb2Name = tk.Label(self.lineupFrame, text="Empty")
        self.rb2Name.grid(row=2, column=1, padx=40, pady=5)

        self.rb2Pts = tk.Label(self.lineupFrame, text="0.0")
        self.rb2Pts.grid(row=2, column=2, padx=40, pady=5)
        # WR1 Row
        self.wr1Label = tk.Label(self.lineupFrame, text="WR")
        self.wr1Label.grid(row=3, column=0, padx=40, pady=5)

        self.wr1Name = tk.Label(self.lineupFrame, text="Empty")
        self.wr1Name.grid(row=3, column=1, padx=40, pady=5)

        self.wr1Pts = tk.Label(self.lineupFrame, text="0.0")
        self.wr1Pts.grid(row=3, column=2, padx=40, pady=5)
        # WR2 Row
        self.wr2Label = tk.Label(self.lineupFrame, text="WR")
        self.wr2Label.grid(row=4, column=0, padx=40, pady=5)

        self.wr2Name = tk.Label(self.lineupFrame, text="Empty")
        self.wr2Name.grid(row=4, column=1, padx=40, pady=5)

        self.wr2Pts = tk.Label(self.lineupFrame, text="0.0")
        self.wr2Pts.grid(row=4, column=2, padx=40, pady=5)
        # TE Row
        self.teLabel = tk.Label(self.lineupFrame, text="TE")
        self.teLabel.grid(row=5, column=0, padx=40, pady=5)

        self.teName = tk.Label(self.lineupFrame, text="Empty")
        self.teName.grid(row=5, column=1, padx=40, pady=5)

        self.tePts = tk.Label(self.lineupFrame, text="0.0")
        self.tePts.grid(row=5, column=2, padx=40, pady=5)
        # FLEX Row
        self.flexLabel = tk.Label(self.lineupFrame, text="FLEX")
        self.flexLabel.grid(row=6, column=0, padx=40, pady=5)

        self.flexName = tk.Label(self.lineupFrame, text="Empty")
        self.flexName.grid(row=6, column=1, padx=40, pady=5)

        self.flexPts = tk.Label(self.lineupFrame, text="0.0")
        self.flexPts.grid(row=6, column=2, padx=40, pady=5)
        # D/ST Row
        self.dstLabel = tk.Label(self.lineupFrame, text="D/ST")
        self.dstLabel.grid(row=7, column=0, padx=40, pady=5)

        self.dstName = tk.Label(self.lineupFrame, text="Empty")
        self.dstName.grid(row=7, column=1, padx=40, pady=5)

        self.dstPts = tk.Label(self.lineupFrame, text="0.0")
        self.dstPts.grid(row=7, column=2, padx=40, pady=5)
        # K Row
        self.kLabel = tk.Label(self.lineupFrame, text="K")
        self.kLabel.grid(row=8, column=0, padx=40, pady=5)

        self.kName = tk.Label(self.lineupFrame, text="Empty")
        self.kName.grid(row=8, column=1, padx=40, pady=5)

        self.kPts = tk.Label(self.lineupFrame, text="0.0")
        self.kPts.grid(row=8, column=2, padx=40, pady=5)

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
