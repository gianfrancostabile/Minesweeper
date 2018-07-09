from .celd import Celd
from .maptype import MapType
from random import randint

class Map(object):

	def __init__(self):
		self.celds = []
		self.difficultSelected = MapType()

	def __init__(self, difficulty):
		self.celds = [[difficulty.height] * difficulty.width for i in range(difficulty.width)]
		self.difficultSelected = difficulty
		self.generate_map(difficulty)

	def generate_map(self, difficulty):
		try:
			for y in range(0, difficulty.height):
				for x in range(0, difficulty.width):
					self.celds[y][x] = Celd(x, y)

			self.putMines()
			self.putNumbers()
		except Exception as e:
			print(e)

	def putMines(self):
		mines = self.difficultSelected.mines
		i = 0

		while i < mines:
			y = randint(0, self.difficultSelected.height-1)
			x = randint(0, self.difficultSelected.width-1)

			if self.celds[y][x].content != -1:
				self.celds[y][x].change_to_mine()
				i = i + 1

	def putNumbers(self):
		for y in range(0, self.difficultSelected.height):
			for x in range(0, self.difficultSelected.width):
				mines = self.countMinesAround(x, y)
				self.celds[y][x].change_to_number(mines)

	def countMinesAround(self, x, y):
		mines, countX, countY = -1, 0, 0
		x2, y2 = x-1, y-1

		if self.celds[y][x].content != -1:
			mines = 0
			while countY < 3:
				while countX < 3:
					if y2 >= 0 and x2 >= 0 and y2 < self.difficultSelected.height and x2 < self.difficultSelected.width and self.celds[y2][x2].content == -1:
						mines = mines + 1
					countX = countX + 1
					x2 = x2 + 1
				countY = countY + 1
				y2 = y2 +1
				countX = 0
				x2 = x-1
		return mines

	def showMap(self):
		print()
		for y in range(0, self.difficultSelected.height):
			for x in range(0, self.difficultSelected.width):
				print(self.celds[y][x].content, end=" ")
			print()
		print()
