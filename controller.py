from Player import Player
from Positions import Positions


def checkPos(pos: str) -> bool:
    try:
        Positions(pos)
        return True
    except ValueError:
        print("[WARN]: " + pos)
        return False


def checkNumber(number: float):
    try:
        float(number)
        return True
    except ValueError:
        print("[WARN]: " + str(number))
        return False


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Bind the Add Player button
        self.view.setAddButtonCommand(self.updateModel)

    def updateModel(self) -> bool:
        # Get Player Info to be stored
        name = self.view.getNameEntry()
        pos = self.view.getPosEntry()
        pts = self.view.getPtsEntry()

        # Input validation
        if not checkNumber(pts):
            return self.view.setErrorLabel(1)
        if not checkPos(pos):
            return self.view.setErrorLabel(2)

        # Convert position to proper type
        try:
            posEnum = Positions[pos.upper()]
        except KeyError:
            print("[WARN] Position conversion error: " + str(posEnum))
            return self.view.setErrorLabel(2)

        player = Player(name, posEnum, float(pts))

        # Call the appropriate position updater
        if posEnum == Positions.QB:
            self.updateQb(player)
        elif posEnum == Positions.RB:
            self.updateRb(player)
        elif posEnum == Positions.WR:
            self.updateWr(player)
        elif posEnum == Positions.TE:
            self.updateTe(player)
        elif posEnum == Positions.DST:
            self.updateDst(player)
        elif posEnum == Positions.K:
            self.updateK(player)

        # Calculate totals and add to view
        self.calculateTotals(posEnum)

    def calculateTotals(self, pos: Positions):
        # Calculate the different point totals in model
        if not Positions(pos) == Positions.BE:
            self.model.starterPts = self.model.calcStarters()
        self.model.totalPts = self.model.calcFullLineup()

        # Update view with point totals
        self.view.setStarterPts(self.model.starterPts)
        self.view.setTotalPts(self.model.totalPts)

        # Handle calculating bench pts
        self.view.setBenchPts(self.view.getTotalPts() - self.view.getStarterPts())

    # Position updaters
    def updateQb(self, player) -> bool:
        if not self.view.getQb():
            self.model.addPlayerData(player)
            self.view.setQbName(player.name)
            self.view.setQbPts(player.pts)
        elif not self.view.getBeFull():
            self.setNextBe(player)
        else:
            return self.view.setErrorLabel(3)
        
        return self.view.setErrorLabel(0)

    def updateRb(self, player) -> bool:
        if not self.view.getRb1():
            self.model.addPlayerData(player)
            self.view.setRb1Name(player.name)
            self.view.setRb1Pts(player.pts)
        elif not self.view.getRb2():
            self.model.addPlayerData(player)
            self.view.setRb2Name(player.name)
            self.view.setRb2Pts(player.pts)
        elif not self.view.getFlex():
            player.pos = Positions.FLEX
            self.model.addPlayerData(player)
            self.view.setFlexName(player.name)
            self.view.setFlexPts(player.pts)
        elif not self.view.getBeFull():
            self.setNextBe(player)
        else:
            return self.view.setErrorLabel(3)
        
        return self.view.setErrorLabel(0)

    def updateWr(self, player) -> bool:
        if not self.view.getWr1():
            self.model.addPlayerData(player)
            self.view.setWr1Name(player.name)
            self.view.setWr1Pts(player.pts)
        elif not self.view.getWr2():
            self.model.addPlayerData(player)
            self.view.setWr2Name(player.name)
            self.view.setWr2Pts(player.pts)
        elif not self.view.getFlex():
            player.pos = Positions.FLEX
            self.model.addPlayerData(player)
            self.view.setFlexName(player.name)
            self.view.setFlexPts(player.pts)
        elif not self.view.getBeFull():
            self.setNextBe(player)
        else:
            return self.view.setErrorLabel(3)
        
        return self.view.setErrorLabel(0)

    def updateTe(self, player) -> bool:
        if not self.view.getTe():
            self.model.addPlayerData(player)
            self.view.setTeName(player.name)
            self.view.setTePts(player.pts)
        elif not self.view.getFlex():
            player.pos = Positions.FLEX
            self.model.addPlayerData(player)
            self.view.setFlexName(player.name)
            self.view.setFlexPts(player.pts)
        elif not self.view.getBeFull():
            self.setNextBe(player)
        else:
            return self.view.setErrorLabel(3)
        
        return self.view.setErrorLabel(0)

    def updateDst(self, player) -> bool:
        if not self.view.getDst():
            self.model.addPlayerData(player)
            self.view.setDstName(player.name)
            self.view.setDstPts(player.pts)
        elif not self.view.getBeFull():
            self.setNextBe(player)
        else:
            return self.view.setErrorLabel(3)

        return self.view.setErrorLabel(0)
    
    def updateK(self, player) -> bool:
        if not self.view.getK():
            self.model.addPlayerData(player)
            self.view.setKName(player.name)
            self.view.setKPts(player.pts)
        elif not self.view.getBeFull():
            self.setNextBe(player)
        else:
            return self.view.setErrorLabel(3)
        
        return self.view.setErrorLabel(0)

    # Bench helper
    def setNextBe(self, player) -> bool:
        # Bench slots 1-7
        for i in range(1, 8):
            name = getattr(self.view, f"be{i}NameVar")
            pts = getattr(self.view, f"be{i}PtsVar")
            if name.get() == "Empty":
                # Update the view
                name.set(player.name)
                pts.set(str(player.pts))
                
                # Update the model
                player.pos = Positions.BE
                self.model.addPlayerData(player)
                return True

        return self.view.setErrorLabel(3)
