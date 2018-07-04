from .maptype import MapType
from .celd import Celd

class Map(object):

	def __init__(self):
		self.maps = {
			"Easy": MapType(9, 9, 10),
			"Medium": MapType(16, 16, 40),
			"Hard": MapType(30, 16, 99)
		}

	def showDifficulty(self):
		for k, v in self.maps.items():
			print("(" + k + ") " + v.getthis())

	def verifyDifficulty(self, difficulty_selected):
		if difficulty_selected in self.maps:
			return self.maps[difficulty_selected]
		else:
			raise Exception("400 - Map type \"{difficulty}\" doesn\'t exists".format(difficulty = difficulty_selected))

	def generate_map(self, difficulty):
		try:
			self.map = {}
			map_type = self.verifyDifficulty(difficulty)
			print(map_type.getthis())
			for x in range(1, map_type.width):
				for y in range(1, map_type.height):
					self.map[str(x) + "-" + str(y)] = Celd()

		except Exception as e:
			print(e)

	def showmap(self):
		for k, v in self.map.items():
			print(v.content, end=", ")