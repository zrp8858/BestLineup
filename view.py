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

        self.errMsgVar = tk.StringVar(value="Enter player info above")
        self.errorLabel = tk.Label(self, textvariable=self.errMsgVar, anchor="center", justify="center")
        self.errorLabel.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

        # Best lineup frame initialization
        self.lineupFrame = tk.Frame(self)
        self.lineupFrame.grid(row=3, column=0, columnspan=4)
        self.displayEmptyLineup()

        # Create lineup rows
        self.addDisplayRow(self.lineupFrame, 0, "QB", self.qbNameVar, self.qbPtsVar)
        self.addDisplayRow(self.lineupFrame, 1, "RB", self.rb1NameVar, self.rb1PtsVar)
        self.addDisplayRow(self.lineupFrame, 2, "RB", self.rb2NameVar, self.rb2PtsVar)
        self.addDisplayRow(self.lineupFrame, 3, "WR", self.wr1NameVar, self.wr1PtsVar)
        self.addDisplayRow(self.lineupFrame, 4, "WR", self.wr2NameVar, self.wr2PtsVar)
        self.addDisplayRow(self.lineupFrame, 5, "TE", self.teNameVar, self.tePtsVar)
        self.addDisplayRow(
            self.lineupFrame, 6, "FLEX", self.flexNameVar, self.flexPtsVar
        )
        self.addDisplayRow(self.lineupFrame, 7, "D/ST", self.dstNameVar, self.dstPtsVar)
        self.addDisplayRow(self.lineupFrame, 8, "K", self.kNameVar, self.kPtsVar)
        # Bench
        for i in range(1, 8):
            nameVar = getattr(self, f"be{i}NameVar")
            ptsVar = getattr(self, f"be{i}PtsVar")
            self.addDisplayRow(self.lineupFrame, 8 + i, "BE", nameVar, ptsVar)

    def displayEmptyLineup(self):
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

        # Bench
        for i in range(1, 8):
            setattr(self, f"be{i}NameVar", tk.StringVar(value="Empty"))
            setattr(self, f"be{i}PtsVar", tk.StringVar(value="0.0"))

    def addDisplayRow(self, parent, row, label, nameVar, ptsVar):
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

    def setErrorLabel(self, num) -> bool:
        errMsg = ""
        match num:
            case 0:
                self.errMsgVar.set("Updated Lineup Successfully!")
                return True
            case 1:
                errMsg = f"Invalid input for points, please enter a decimal value!"
            case 2:
                errMsg = f"Invalid position, please enter QB, RB, WR, TE, D/ST or K!"
            case 3:
                errMsg = f"All available slots for this position are full!"
        
        self.errMsgVar.set(errMsg)
        return False

    # Button binding
    def setButtonCommand(self, command):
        self.button.config(command=command)
