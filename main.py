from ursina import Ursina
from ursina import Animation
from ursina import destroy

app = Ursina()

zahl = 7
short = Animation('7', scale=(9, 5), loop=True, autoplay=True)


def update():
    pass


def input(key):
    global short, zahl
    if key == 'scroll up' and zahl != 13:
        zahl += 1
        destroy(short)
        short = Animation(f'{zahl}', scale=(7, 4), loop=True, autoplay=True)
    if key == 'scroll down' and zahl != 1:
        zahl -= 1
        destroy(short)
        short = Animation(f'{zahl}', scale=(7, 4), loop=True, autoplay=True)


app.run()
