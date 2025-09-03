import tkinter as tk
from Positions import Positions


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

        self.addButton = tk.Button(self, text="Add Player")
        self.addButton.grid(row=1, column=3, padx=10, pady=10)

        self.errMsgVar = tk.StringVar(value="Enter player info above")
        self.errorLabel = tk.Label(
            self, textvariable=self.errMsgVar, anchor="center", justify="center"
        )
        self.errorLabel.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

        # New Frame:
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
        self.addDisplayRow(
            self.lineupFrame, 8, "K", self.kNameVar, self.kPtsVar, beSpace=(5, 10)
        )  # Includes space b/t kicker and starters pts

        # Total score for starters
        self.addDisplayRow(
            self.lineupFrame, 9, "", "Starters:", self.starterPtsVar, beSpace=(5, 20)
        )  # Includes space b/t starters pts and bench

        # Bench
        self.addDisplayRow(self.lineupFrame, 10, "BE", self.be1NameVar, self.be1PtsVar)
        self.addDisplayRow(self.lineupFrame, 11, "BE", self.be2NameVar, self.be2PtsVar)
        self.addDisplayRow(self.lineupFrame, 12, "BE", self.be3NameVar, self.be3PtsVar)
        self.addDisplayRow(self.lineupFrame, 13, "BE", self.be4NameVar, self.be4PtsVar)
        self.addDisplayRow(self.lineupFrame, 14, "BE", self.be5NameVar, self.be5PtsVar)
        self.addDisplayRow(self.lineupFrame, 15, "BE", self.be6NameVar, self.be6PtsVar)
        self.addDisplayRow(self.lineupFrame, 16, "BE", self.be7NameVar, self.be7PtsVar)

        # Total score for bench
        self.addDisplayRow(
            self.lineupFrame, 17, "", "Bench:", self.benchPtsVar, beSpace=(10, 5)
        )
        # Total score for full team
        self.addDisplayRow(
            self.lineupFrame, 18, "", "Total:", self.totalPtsVar, beSpace=(10, 20)
        )  # Includes space b/t bench players and total/total and bottom of screen

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

        # Total starter pts
        self.starterPtsVar = tk.StringVar(value="0.0")

        # Bench
        self.be1NameVar = tk.StringVar(value="Empty")
        self.be1PtsVar = tk.StringVar(value="0.0")

        self.be2NameVar = tk.StringVar(value="Empty")
        self.be2PtsVar = tk.StringVar(value="0.0")

        self.be3NameVar = tk.StringVar(value="Empty")
        self.be3PtsVar = tk.StringVar(value="0.0")

        self.be4NameVar = tk.StringVar(value="Empty")
        self.be4PtsVar = tk.StringVar(value="0.0")

        self.be5NameVar = tk.StringVar(value="Empty")
        self.be5PtsVar = tk.StringVar(value="0.0")

        self.be6NameVar = tk.StringVar(value="Empty")
        self.be6PtsVar = tk.StringVar(value="0.0")

        self.be7NameVar = tk.StringVar(value="Empty")
        self.be7PtsVar = tk.StringVar(value="0.0")

        # Bench pts
        self.benchPtsVar = tk.StringVar(value="0.0")
        # Total pts
        self.totalPtsVar = tk.StringVar(value="0.0")

    # Generic function for adding any three-column row in lineupFrame
    def addDisplayRow(self, parent, row, first, second, third, beSpace=(5, 5)):
        for col, value in enumerate([first, second, third]):
            if isinstance(value, tk.StringVar):
                tk.Label(parent, textvariable=value).grid(
                    row=row, column=col, padx=40, pady=beSpace
                )
            else:
                tk.Label(parent, text=value).grid(
                    row=row, column=col, padx=40, pady=beSpace
                )

    # Entry getters
    def getNameEntry(self):
        return self.nameEntry.get()

    def getPosEntry(self):
        return self.positionEntry.get()

    def getPtsEntry(self):
        return self.pointsEntry.get()

    # Slot getters
    def getQb(self) -> bool:
        return self.qbNameVar.get() != "Empty"

    def getRb1(self) -> bool:
        return self.rb1NameVar.get() != "Empty"

    def getRb2(self) -> bool:
        return self.rb2NameVar.get() != "Empty"

    def getWr1(self) -> bool:
        return self.wr1NameVar.get() != "Empty"

    def getWr2(self) -> bool:
        return self.wr2NameVar.get() != "Empty"

    def getTe(self) -> bool:
        return self.teNameVar.get() != "Empty"

    def getFlex(self) -> bool:
        return self.flexNameVar.get() != "Empty"

    def getDst(self) -> bool:
        return self.dstNameVar.get() != "Empty"

    def getK(self) -> bool:
        return self.kNameVar.get() != "Empty"

    # Starter Pts
    def getStarterPts(self) -> float:
        return float(self.starterPtsVar.get())

    # Bench Full
    def getBeFull(self) -> bool:
        return self.be7NameVar.get() != "Empty"

    # Total Pts
    def getTotalPts(self) -> float:
        return float(self.totalPtsVar.get())

    # Slot setters
    def setSlot(self, slot: str, name: str, pts: float):
        nameMethod = f"set{slot}Name"
        ptsMethod = f"set{slot}Pts"

        if hasattr(self, nameMethod) and hasattr(self, ptsMethod):
            getattr(self, nameMethod)(name)
            getattr(self, ptsMethod)(pts)
            self.calcViewUpdates(slot)
        else:
            raise ValueError(f"Invalid slot: {slot}")

    def slotToPos(slot: str) -> Positions:
        if slot.startswith("qb"):
            return Positions.QB
        elif slot.startswith("rb"):
            return Positions.RB
        elif slot.startswith("wr"):
            return Positions.WR
        elif slot.startswith("te"):
            return Positions.TE
        elif slot.startswith("dst"):
            return Positions.DST
        elif slot.startswith("k"):
            return Positions.K

        return Positions.BE

    # Starting Lineup
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

    # Starter Pts
    def setStarterPts(self, text):
        self.starterPtsVar.set(str(text))

    # Bench
    def setBe1Name(self, text):
        self.be1NameVar.set(text)

    def setBe1Pts(self, text):
        self.be1PtsVar.set(str(text))

    def setBe2Name(self, text):
        self.be2NameVar.set(text)

    def setBe2Pts(self, text):
        self.be2PtsVar.set(str(text))

    def setBe3Name(self, text):
        self.be3NameVar.set(text)

    def setBe3Pts(self, text):
        self.be3PtsVar.set(str(text))

    def setBe4Name(self, text):
        self.be4NameVar.set(text)

    def setBe4Pts(self, text):
        self.be4PtsVar.set(str(text))

    def setBe5Name(self, text):
        self.be5NameVar.set(text)

    def setBe5Pts(self, text):
        self.be5PtsVar.set(str(text))

    def setBe6Name(self, text):
        self.be6NameVar.set(text)

    def setBe6Pts(self, text):
        self.be6PtsVar.set(str(text))

    def setBe7Name(self, text):
        self.be7NameVar.set(text)

    def setBe7Pts(self, text):
        self.be7PtsVar.set(str(text))

    # Bench Pts
    def setBenchPts(self, text):
        self.benchPtsVar.set(str(text))
    # Total Pts
    def setTotalPts(self, text):
        self.totalPtsVar.set(str(text))

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
    def setAddButtonCommand(self, command):
        self.addButton.config(command=command)
