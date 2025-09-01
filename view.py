import tkinter as tk


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Best Lineup Calculator")

        # Entry fields
        tk.Label(self, text="Name").grid(row=0, column=0, padx=10)
        tk.Label(self, text="Position").grid(row=0, column=1, padx=10)
        tk.Label(self, text="Points").grid(row=0, column=2, padx=10)

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

        # Best lineup frame
        self.lineupFrame = tk.Frame(self)
        self.lineupFrame.grid(row=3, column=0, columnspan=4)

        # Initialize StringVars for all positions
        self._init_player_vars()

        # Create lineup rows
        self._create_row(self.lineupFrame, 0, "QB", self.qbNameVar, self.qbPtsVar)
        self._create_row(self.lineupFrame, 1, "RB", self.rb1NameVar, self.rb1PtsVar)
        self._create_row(self.lineupFrame, 2, "RB", self.rb2NameVar, self.rb2PtsVar)
        self._create_row(self.lineupFrame, 3, "WR", self.wr1NameVar, self.wr1PtsVar)
        self._create_row(self.lineupFrame, 4, "WR", self.wr2NameVar, self.wr2PtsVar)
        self._create_row(self.lineupFrame, 5, "TE", self.teNameVar, self.tePtsVar)
        self._create_row(self.lineupFrame, 6, "FLEX", self.flexNameVar, self.flexPtsVar)
        self._create_row(self.lineupFrame, 7, "D/ST", self.dstNameVar, self.dstPtsVar)
        self._create_row(self.lineupFrame, 8, "K", self.kNameVar, self.kPtsVar)
        # Bench
        for i in range(1, 8):
            nameVar = getattr(self, f"be{i}NameVar")
            ptsVar = getattr(self, f"be{i}PtsVar")
            self._create_row(self.lineupFrame, 8 + i, "BE", nameVar, ptsVar)

    def _init_player_vars(self):
        # Main lineup
        self.qbNameVar = tk.StringVar(value="Empty")
        self.qbPtsVar = tk.StringVar(value="0.0")

        self.rb1NameVar = tk.StringVar(value="Empty")
        self.rb1PtsVar = tk.StringVar(value="0.0")

        self.rb2NameVar = tk.StringVar(value="Empty")
        self.rb2PtsVar = tk.StringVar(value="0.0")

        self.wr1NameVar = tk.StringVar(value="Empty")
        self.wr1PtsVar = tk.StringVar(value="0.0")

        self.wr2NameVar = tk.StringVar(value="Empty")
        self.wr2PtsVar = tk.StringVar(value="0.0")

        self.teNameVar = tk.StringVar(value="Empty")
        self.tePtsVar = tk.StringVar(value="0.0")

        self.flexNameVar = tk.StringVar(value="Empty")
        self.flexPtsVar = tk.StringVar(value="0.0")

        self.dstNameVar = tk.StringVar(value="Empty")
        self.dstPtsVar = tk.StringVar(value="0.0")

        self.kNameVar = tk.StringVar(value="Empty")
        self.kPtsVar = tk.StringVar(value="0.0")

        self.benchNameVars = [None] + [tk.StringVar(value="Empty") for _ in range(1, 8)]
        self.benchPtsVars = [None] + [tk.StringVar(value="0.0") for _ in range(1, 8)]

        self.errNumVar = tk.StringVar(value="")
        self.errPosVar = tk.StringVar(value="N/A")

        # Bench
        for i in range(1, 8):
            setattr(self, f"be{i}NameVar", tk.StringVar(value="Empty"))
            setattr(self, f"be{i}PtsVar", tk.StringVar(value="0.0"))

    def _create_row(self, parent, row, label, nameVar, ptsVar):
        tk.Label(parent, text=label).grid(row=row, column=0, padx=40, pady=5)
        tk.Label(parent, textvariable=nameVar).grid(row=row, column=1, padx=40, pady=5)
        tk.Label(parent, textvariable=ptsVar).grid(row=row, column=2, padx=40, pady=5)

    # Entry getters
    def getNameEntry(self):
        return self.nameEntry.get()

    def getPosEntry(self):
        return self.positionEntry.get()

    def getPtsEntry(self):
        return self.pointsEntry.get()

    # Slot getters
    def getQb(self):
        return self.qbNameVar.get() != "Empty"

    def getRb1(self):
        return self.rb1NameVar.get() != "Empty"

    def getRb2(self):
        return self.rb2NameVar.get() != "Empty"

    def getWr1(self):
        return self.wr1NameVar.get() != "Empty"

    def getWr2(self):
        return self.wr2NameVar.get() != "Empty"

    def getTe(self):
        return self.teNameVar.get() != "Empty"

    def getFlex(self):
        return self.flexNameVar.get() != "Empty"

    def getDst(self):
        return self.dstNameVar.get() != "Empty"

    def getK(self):
        return self.kNameVar.get() != "Empty"

    def getBeFull(self):
        return all(getattr(self, f"be{i}NameVar").get() != "Empty" for i in range(1, 8))

    # Slot setters
    def setQbName(self, text):
        self.qbNameVar.set(text)

    def setQbPts(self, text):
        self.qbPtsVar.set(str(text))

    def setRb1Name(self, text):
        self.rb1NameVar.set(text)

    def setRb1Pts(self, text):
        self.rb1PtsVar.set(str(text))

    def setRb2Name(self, text):
        self.rb2NameVar.set(text)

    def setRb2Pts(self, text):
        self.rb2PtsVar.set(str(text))

    def setWr1Name(self, text):
        self.wr1NameVar.set(text)

    def setWr1Pts(self, text):
        self.wr1PtsVar.set(str(text))

    def setWr2Name(self, text):
        self.wr2NameVar.set(text)

    def setWr2Pts(self, text):
        self.wr2PtsVar.set(str(text))

    def setTeName(self, text):
        self.teNameVar.set(text)

    def setTePts(self, text):
        self.tePtsVar.set(str(text))

    def setFlexName(self, text):
        self.flexNameVar.set(text)

    def setFlexPts(self, text):
        self.flexPtsVar.set(str(text))

    def setDstName(self, text):
        self.dstNameVar.set(text)

    def setDstPts(self, text):
        self.dstPtsVar.set(str(text))

    def setKName(self, text):
        self.kNameVar.set(text)

    def setKPts(self, text):
        self.kPtsVar.set(str(text))

    def setBeName(self, num, text):
        self.benchNameVars[num].set(text)

    def setBePts(self, num, text):
        self.benchPtsVars[num].set(str(text))

    def setErrNum(self, num):
        self.errNumVar.set(num)

    def setErrPos(self, pos):
        self.errPosVar.set(pos)

    # Button binding
    def setButtonCommand(self, command):
        self.button.config(command=command)
