from typing import List
from player import Player
from positions import FantasyPositions, NflPositions


def checkPos(pos: str) -> bool:
    try:
        FantasyPositions(pos)
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

        # Bind add and sort buttons
        self.view.setAddButtonCommand(self.updateModel)
        self.view.setSortButtonCommand(self.findBestLineup)

    # Logic for adding a player to lineup
    def updateModel(self):
        # Get Player Info to be stored
        name = self.view.getNameEntry()
        nflPos = self.view.getNflPosEntry()
        pos = self.view.getPosEntry()
        pts = self.view.getPtsEntry()

        # Input validation
        if not checkNumber(pts):
            return self.view.setErrorLabel(1)
        if not checkPos(pos):
            return self.view.setErrorLabel(2)

        # Convert position to proper type
        try:
            nflPosEnum = NflPositions[nflPos.upper()]
            posEnum = FantasyPositions[pos.upper()]
        except KeyError:
            print(
                "[WARN] Position(s) conversion error: "
                + str(posEnum)
                + ", "
                + str(nflPosEnum)
            )
            return self.view.setErrorLabel(2)

        player = Player(name, nflPosEnum, posEnum, float(pts))

        # Call the appropriate position updater
        if nflPosEnum == NflPositions.QB:
            self.updateQb(player)
        elif nflPosEnum == NflPositions.RB:
            self.updateRb(player)
        elif nflPosEnum == NflPositions.WR:
            self.updateWr(player)
        elif nflPosEnum == NflPositions.TE:
            self.updateTe(player)
        elif nflPosEnum == NflPositions.DST:
            self.updateDst(player)
        elif nflPosEnum == NflPositions.K:
            self.updateK(player)

        # Calculate totals and add to view
        self.calculateTotals(posEnum)

    def calculateTotals(self, pos: FantasyPositions):
        # Calculate the different point totals in model
        if not FantasyPositions(pos) == FantasyPositions.BE:
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
            player.pos = FantasyPositions.FLEX
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
            player.pos = FantasyPositions.FLEX
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
            player.pos = FantasyPositions.FLEX
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
                player.pos = FantasyPositions.BE
                self.model.addPlayerData(player)
                return True

        return self.view.setErrorLabel(3)

    # Logic for sorting players in lineup
    def findBestLineup(self) -> List[Player]:
        # Final Sorted Lineup in order displayed on UI
        bestLineup: List[Player] = []

        # 1. Add top for each position if they exist
        bestLineup.extend(self.model.getQbs()[:1])
        bestLineup.extend(self.model.getRbs()[:2])
        bestLineup.extend(self.model.getWrs()[:2])
        bestLineup.extend(self.model.getTes()[:1])
        # 2. Generate flex top lineup
        bestLineup.extend(self.filterFlex(self.model.getFlexs())[:1])
        # 3. Add dst and k
        bestLineup.extend(self.model.getDsts()[:1])
        bestLineup.extend(self.model.getKs()[:1])
        # 4. Add rest of lineup to bench sorted
        for player in self.filterBench():
            bestLineup.append(player)

        return bestLineup
    
    def filterBench(self) -> List[Player]:
        # Get players that are not in starting lineup
        benchPlayers: List[Player] = []
        # Qbs
        for qb in self.model.getQbs()[1:]: # exclude starter
            benchPlayers.append(qb)
        # Non-Flex players
        for flex in self.filterFlex(self.model.getFlexs())[1:]: # exclude flex leader
            benchPlayers.append(flex)
        # Dsts
        for dst in self.model.getDsts()[1:]:
            benchPlayers.append(dst)
        # K
        for k in self.model.getKs()[1:]:
            benchPlayers.append(k)

        # Return the sorted list
        return sorted(
            [player for player in benchPlayers],
            key=lambda p: p.pts,
            reverse=True,
        )

    def filterFlex(self, flexOpts: List[Player]) -> List[Player]:
        # Remove starting players that could be in flexOpts
        rbCount = 0
        wrCount = 0
        teCount = 0

        filtered: List[Player] = []

        for player in flexOpts:
            if player.nflPos == NflPositions.RB and rbCount < 2:
                rbCount += 1
                continue
            if player.nflPos == NflPositions.WR and wrCount < 2:
                wrCount += 1
                continue
            if player.nflPos == NflPositions.TE and teCount < 1:
                teCount += 1
                continue

            filtered.append(player)

        return filtered
