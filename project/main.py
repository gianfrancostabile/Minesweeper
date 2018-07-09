from models.map import Map
from models.maptype import MapType
from models.view import View

types = {
    "Easy": MapType(9, 9, 10),
    "Medium": MapType(16, 16, 40),
    "Hard": MapType(30, 16, 99)
}

def main():
    difficulty = None

    loop = False
    while not loop:
        try:
            showTypes()
            print("Which difficulty do you choose? ", end=" ")
            difficultyStr = str(input())
            difficulty = getDifficulty(difficultyStr)
            loop = True

        except Exception as e:
            print(str(e) + " Write a correct difficulty...\n")

    mMap = Map(difficulty)
    view = View()
    view.generateFrameGrids(mMap)
    view.display()

def getDifficulty(difficulty_selected):
    if difficulty_selected in types:
        return types[difficulty_selected]
    else:
        raise Exception("\n400 - Map type \"{difficulty}\" doesn\'t exists.".format(difficulty=difficulty_selected))

def showTypes():
    for k, v in types.items():
        print("({difficulty}) - {map_type}".format(difficulty=k, map_type=v.getThis()))

if __name__ == "__main__":
    main()

