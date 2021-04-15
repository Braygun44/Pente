class penteSetup:
	def __init__(self, sWidth, sHeight):
		self.sWidth = sWidth
		self.sHeight = sHeight

		#board params
		self.boardStartXY = (self.sWidth * 0.05, self.sHeight * 0.05)
		self.boardSizeSize = self.sHeight * 0.1

		#scoreboard params
		self.scoreWinXY = (self.sWidth * 0.15 + self.boardSizeSize, self.sHeight * 0.05, self.sHeight * 0.10)
		self.scoreWinHW = (self.boardSizeSize * (7/16), self.sHeight * 0.10)

	def getBoardSizeSide(self):
		return self.boardSizeSize

	def getBoardParams(self):
		return (self.boardStartXY[0], self.boardStartXY[1], self.boardSizeSize, self.boardSizeSize)

	def getScoreBParams(self):
		return (self.scoreWinXY[0], self.scoreWinXY[1], self.scoreWinHW[0], self.scoreWinHW[1])