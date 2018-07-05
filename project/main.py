from models.map import Map
from models.maptype import MapType

class Main(object):

    def __init__(self):
        self.types = {}

    def main(self):
        self.generateMapTypes()
        difficulty = None

        loop = False
        while not loop:
            try:
                self.showTypes()
                print("Which difficulty do you choose? ", end=" ")
                difficultyStr = str(input())
                difficulty = self.getDifficulty(difficultyStr)
                loop = True

            except Exception as e:
                print(str(e) + " Write a correct difficulty...\n")

        mMap = Map(difficulty)
        mMap.showMap()

    def generateMapTypes(self):
        self.types = {
            "Easy": MapType(9, 9, 10),
            "Medium": MapType(16, 16, 40),
            "Hard": MapType(30, 16, 99)
        }

    def getDifficulty(self, difficulty_selected):
        if difficulty_selected in self.types:
            return self.types[difficulty_selected]
        else:
            raise Exception("\n400 - Map type \"{difficulty}\" doesn\'t exists.".format(difficulty=difficulty_selected))

    def showTypes(self):
        for k, v in self.types.items():
            print("({difficulty}) - {map_type}".format(difficulty=k, map_type=v.getThis()))

if __name__ == "__main__":
    start = Main()
    start.main()
