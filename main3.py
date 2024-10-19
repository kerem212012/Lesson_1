WIDTH = 300
HEIGHT = 300

TITLE = "Ghost in Tower"
FPS = 30


ghost = Actor('ghost', (150, 150))
fon = Actor("bg")

def draw():
    fon.draw()
    ghost.draw()

def update(dt):
    if keyboard.left and ghost.x > 20:
        ghost.x = ghost.x - 5
    elif keyboard.right and ghost.x < 280:
        ghost.x = ghost.x + 5
    elif keyboard.up and ghost.y > 30:
        ghost.y = ghost.y - 5
    elif keyboard.down and ghost.y < 265:
        ghost.y = ghost.y + 5