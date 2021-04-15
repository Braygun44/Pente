class penteSetup:
    def __init__(self, sWidth, sHeight):
        self.sWidth = sWidth
        self.sHeight = sHeight
        #playboard parameters
        self.boardStartXY = ( self.sWidth * 0.05, self.sHeight * 0.025 )
        self.boardSizeWH = self.sHeight - self.sHeight * 0.05
        #scoreboard parameters
        self.scoreWinXY = (self.sWidth * 0.1 + self.boardSizeWH, self.sHeight * 0.025)
        self.scoreWinWH = (self.boardSizeWH * (10 / 16), self.sHeight - self.sHeight * 0.05)

    def newParams(self):
        self.sWidth = sWidth
        self.sHeight = sHeight
        #playboard parameters
        self.boardStartXY = ( self.sWidth * 0.05, self.sHeight * 0.025 )
        self.boardSizeWH = self.sHeight - self.sHeight * 0.05
        #scoreboard parameters
        self.scoreWinXY = (self.sWidth * 0.1 + self.boardSizeWH, self.sHeight * 0.025)
        self.scoreWinWH = (self.boardSizeWH * (10 / 16), self.sHeight - self.sHeight * 0.05)

    def getBoardSizeSide(self):
        return(self.boardSizeWH)

    def getBoardParams(self):
        return(self.boardStartXY[0], self.boardStartXY[1], self.boardSizeWH, self.boardSizeWH)

    def getScoreBParams(self):
        return(self.scoreWinXY[0], self.scoreWinXY[1], self.scoreWinWH[0], self.scoreWinWH[1])