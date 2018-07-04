from models.map import Map

def main():
    mMap = Map()
    mMap.showDifficulty()

    try:
        print("Which difficulty do you choose? ", end=" ")
        difficulty = str(input())
        mMap.generate_map(difficulty)
        mMap.showmap()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
