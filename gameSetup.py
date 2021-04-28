class penteSetup:
    def __init__(self, sWidth, sHeight):
        self.sWidth = sWidth
        self.sHeight = sHeight
        self.mValue = 0.05
        self.spacerValue = self.sHeight * self.mValue
        self.boardStartXY = (self.spacerValue, self.spacerValue)
        self.boardSizeWH = self.sHeight - (self.spacerValue * 2)
        self.scoreWinXY = ((self.spacerValue * 2) + self.boardSizeWH, self.spacerValue)
        self.scoreWinWH = (self.boardSizeWH * (7/16), self.boardSizeWH)
        self.finalWidth = self.spacerValue + self.boardSizeWH + self.spacerValue + self.scoreWinWH[0] + self.spacerValue
        self.finalHeight = self.sHeight

    def getBoardSizeSide(self):
        return(self.boardSizeWH)

    def getBoardParams(self):
        return(self.boardStartXY[0], self.boardStartXY[1], self.boardSizeWH, self.boardSizeWH)

    def getScoreBParams(self):
        return(self.scoreWinXY[0], self.scoreWinXY[1], self.scoreWinWH[0], self.scoreWinWH[1])

    def getFinalW(self):
        return int(self.finalWidth)

    def getFinalH(self):
        return int(self.finalHeight)