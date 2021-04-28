class Square:
	dark_color = 1
	empty = 0
	light_color = -1
#
	bg_color = (242, 215, 167)
	lslategrey = (119, 136, 153)

	def __init__(self, xLoc, yLoc, side):
		self.xLoc = xLoc
		self.yLoc = yLoc
		self.side = side
		self.myState = Square.empty

	def getDrawParams(self):
		return(self.xLoc, self.yLoc, self.side, self.side)
	def getState(self):
		return self.myState
	def getBGColor(self):
		return self.bg_color
	def getLineColor(self):
		return self.lslategrey