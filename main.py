WIDTH = 1550
HEIGHT = 800
pencil = Actor('pencil')
face = Actor('face')
kist = Actor('kist')
mario = Actor('mario')
flower = Actor('flower')
spider = Actor('spider')
superfathero = Actor('superfathero')
pencil.pos = 100, 50
face.pos = 800, 700
kist.pos = 700, 500
mario.pos = 200, 500
flower.pos = 500, 50
spider.pos = 300, 50
superfathero.pos = 30, 50


def draw():
    screen.fill("red")
    pencil.draw()
    face.draw()
    kist.draw()
    mario.draw()
    flower.draw()
    spider.draw()
    superfathero.draw()