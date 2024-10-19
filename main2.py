import time

WIDTH = 600
HEIGHT = 300

FPS = 30

fon = Actor('fon_city')
coddy = Actor('coddy', (50, 240))
fireball = Actor('fireball', (700, 240))


def draw():
    fon.draw()
    coddy.draw()
    fireball.draw()


def update(dt):
    if fireball.x > -20:
        fireball.x = fireball.x - 5
    else:
        fireball.x = WIDTH + 20
    #coddy left and right
    if keyboard.left and coddy.x > 20:
        coddy.x = coddy.x - 5
        coddy.image='coddy_left'
    elif keyboard.right and coddy.x < 580:
        coddy.image='coddy'
        coddy.x = coddy.x + 5



def on_key_down(key):
    if keyboard.up or keyboard.w:
        coddy.y = 100
        coddy.image='coddy_up'
        animate(coddy, tween='bounce_end', duration=2, y=240)