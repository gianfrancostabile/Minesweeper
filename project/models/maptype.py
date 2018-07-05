
class MapType(object):

	def __init__(self):
		self.width = 0
		self.height = 0
		self.mines = 0

	def __init__(self, width, height, mines):
		self.width = width
		self.height = height
		self.mines = mines

	def getThis(self):
		return str(self.width) + "x" + str(self.height) + " - " + str(self.mines) + " mines."



