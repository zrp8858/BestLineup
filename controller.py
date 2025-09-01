from Player import Player
from positions import Positions


def checkPos(pos: str) -> bool:
    try:
        Positions(pos)
        return True
    except ValueError:
        return False


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

        # Bind the Add Player button
        self.view.setButtonCommand(self.updateModel)

    def updateModel(self) -> bool:
        # Get user input
        name = self.view.getNameEntry()
        pos = self.view.getPosEntry()
        pts = self.view.getPtsEntry()

        # Validate input
        if not checkNumber(pts):
            self.view.setErrNum(1)
            return False
        if not checkPos(pos):
            self.view.setErrNum(2)
            return False

        # Create player object
        player = Player(name, pos, float(pts))

        # Call the appropriate position updater
        if pos == Positions.QB.value:
            return self.updateQb(player)
        elif pos == Positions.RB.value:
            return self.updateRb(player)
        elif pos == Positions.WR.value:
            return self.updateWr(player)
        elif pos == Positions.TE.value:
            return self.updateTe(player)
        elif pos == Positions.DST.value:
            return self.updateDst(player)
        elif pos == Positions.K.value:
            return self.updateK(player)

        # If position invalid
        self.view.setErrNum(2)
        return False

    # Position updaters
    def updateQb(self, player) -> bool:
        if not self.view.getQb():
            self.model.addQbData(player)
            self.view.setQbName(player.name)
            self.view.setQbPts(player.pts)
        elif not self.view.getBeFull():
            self.setNextBe(player)
        else:
            self.view.setErrNum(3)
            self.view.setErrPos("QB")
            return False
        self.view.setErrNum(0)
        self.view.setErrPos("QB")
        return True

    def updateRb(self, player) -> bool:
        if not self.view.getRb1():
            self.model.addRb1Data(player)
            self.view.setRb1Name(player.name)
            self.view.setRb1Pts(player.pts)
        elif not self.view.getRb2():
            self.model.addRb2Data(player)
            self.view.setRb2Name(player.name)
            self.view.setRb2Pts(player.pts)
        elif not self.view.getFlex():
            self.model.addFlexData(player)
            self.view.setFlexName(player.name)
            self.view.setFlexPts(player.pts)
        elif not self.view.getBeFull():
            self.setNextBe(player)
        else:
            self.view.setErrNum(3)
            self.view.setErrPos("RB")
            return False
        self.view.setErrNum(0)
        self.view.setErrPos("RB")
        return True

    def updateWr(self, player) -> bool:
        if not self.view.getWr1():
            self.model.addWr1Data(player)
            self.view.setWr1Name(player.name)
            self.view.setWr1Pts(player.pts)
        elif not self.view.getWr2():
            self.model.addWr2Data(player)
            self.view.setWr2Name(player.name)
            self.view.setWr2Pts(player.pts)
        elif not self.view.getFlex():
            self.model.addFlexData(player)
            self.view.setFlexName(player.name)
            self.view.setFlexPts(player.pts)
        elif not self.view.getBeFull():
            self.setNextBe(player)
        else:
            self.view.setErrNum(3)
            self.view.setErrPos("WR")
            return False
        self.view.setErrNum(0)
        self.view.setErrPos("WR")
        return True

    def updateTe(self, player) -> bool:
        if not self.view.getTe():
            self.model.addTeData(player)
            self.view.setTeName(player.name)
            self.view.setTePts(player.pts)
        elif not self.view.getFlex():
            self.model.addFlexData(player)
            self.view.setFlexName(player.name)
            self.view.setFlexPts(player.pts)
        elif not self.view.getBeFull():
            self.setNextBe(player)
        else:
            self.view.setErrNum(3)
            self.view.setErrPos("TE")
            return False
        self.view.setErrNum(0)
        self.view.setErrPos("TE")
        return True

    def updateDst(self, player) -> bool:
        if not self.view.getDst():
            self.model.addDstData(player)
            self.view.setDstName(player.name)
            self.view.setDstPts(player.pts)
        elif not self.view.getBeFull():
            self.setNextBe(player)
        else:
            self.view.setErrNum(3)
            self.view.setErrPos("D/ST")
            return False
        self.view.setErrNum(0)
        self.view.setErrPos("D/ST")
        return True

    def updateK(self, player) -> bool:
        if not self.view.getK():
            self.model.addKData(player)
            self.view.setKName(player.name)
            self.view.setKPts(player.pts)
        elif not self.view.getBeFull():
            self.setNextBe(player)
        else:
            self.view.setErrNum(3)
            self.view.setErrPos("K")
            return False
        self.view.setErrNum(0)
        self.view.setErrPos("K")
        return True

    # Bench helper
    def setNextBe(self, player):
        for i in range(1, 8):
            name_var = getattr(self.view, f"be{i}NameVar")
            pts_var = getattr(self.view, f"be{i}PtsVar")
            if name_var.get() == "Empty":
                # Update view
                name_var.set(player.name)
                pts_var.set(str(player.pts))
                # Update model
                getattr(self.model, f"addBe{i}Data")(player)
                return
