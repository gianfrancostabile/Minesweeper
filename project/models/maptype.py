
class MapType(object):

	def __init__(self, width, height, mines):
		self.width = width
		self.height = height
		self.mines = mines

	def getthis(self):
		return str(self.width) + "x" + str(self.height) + " - " + str(self.mines) + " mines."



