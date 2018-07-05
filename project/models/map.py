from .celd import Celd
from .maptype import MapType

class Map(object):

	def __init__(self):
		self.map = []
		self.difficultSelected = MapType()

	def __init__(self, difficulty):
		self.map = [[difficulty.height] * difficulty.width for i in range(difficulty.width)]
		self.difficultSelected = difficulty
		self.generate_map(difficulty)

	def generate_map(self, difficulty):
		try:
			for y in range(0, difficulty.height):
				for x in range(0, difficulty.width):
					self.map[y][x] = Celd()

		except Exception as e:
			print(e)

	def showMap(self):
		for y in range(0, self.difficultSelected.height):
			for x in range(0, self.difficultSelected.width):
				print(self.map[y][x].content, end=" ")
			print()

