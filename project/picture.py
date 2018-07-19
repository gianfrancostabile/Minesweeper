import pygame


def load_picture(url):
    try:
        picture = pygame.image.load(url)
        picture = picture.convert()
    except pygame.error:
        pass

    return picture


def charge_pictures():
    empty_not_visible = load_picture("images/empty_not_visible.jpg")
    empty_visible = load_picture("images/empty_visible.jpg")

    bomb = load_picture("images/bomb.jpg")
    flag = load_picture("images/flag.png")
    question = load_picture("images/question.png")

    one = load_picture("images/one.png")
    two = load_picture("images/two.png")
    three = load_picture("images/three.png")
    four = load_picture("images/four.png")
    five = load_picture("images/five.png")
    six = load_picture("images/six.png")
    seven = load_picture("images/seven.png")
    eight = load_picture("images/eight.png")

    pictures = {
        "empty": empty_not_visible,
        0: empty_visible,
        9: bomb,
        "flag": flag,
        "question": question,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight
    }

    return pictures

PICTURES = charge_pictures()

def get_picture(content):
    global PICTURE
    return PICTURES.get(content)