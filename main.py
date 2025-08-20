from ursina import Ursina
from ursina import Animation
from ursina import Sky
from ursina import color
from ursina import application
from ursina import Text
from ursina import destroy

app = Ursina()
Sky(color=color.black)

zahl = 7
short = Animation('7', scale=(9, 5), loop=True, autoplay=True, z=-1)

text = Text(text='`Minecraft mini Tiktok`', position=(-0.3, 0.4), color=color.gold, scale=2)


def update():
    pass


def input(key):
    global short, zahl
    if key == 'escape' or key == 'q':
        application.quit()
    if key == 'scroll up' and zahl != 15:
        zahl += 1
        destroy(short)
        short = Animation(f'{zahl}', scale=(7, 4), loop=True, autoplay=True)
    if key == 'scroll down' and zahl != 1:
        zahl -= 1
        destroy(short)
        short = Animation(f'{zahl}', scale=(7, 4), loop=True, autoplay=True)


app.run()
