import pygame as pg
import settings
from player import Player

pg.init()

screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
pg.display.set_caption("Platformer")
background = pg.image.load("data/background/backgroung.png").convert()
background = pg.transform.scale(background, (settings.WIDTH, settings.HEIGHT))

pg.mixer.music.load("data/audio/song_forest.mp3")
pg.mixer.music.play(-1)

clock = pg.time.Clock()

player = Player(50, settings.HEIGHT - 100, 'data/player/holding/right/Idle1.png')
running = True

while running:
    screen.fill("black")
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYUP:
            player.move = False

    key = pg.key.get_pressed()
    if key[pg.K_RIGHT] or key[pg.K_d]:
        player.dx = 5
        player.move = True
        player.left = False
        player.right = True
    
    if key[pg.K_LEFT] or key[pg.K_a]:
        player.dx = -5
        player.move = True
        player.left = True
        player.right = False
    
    if key[pg.K_UP] or key[pg.K_w]:
        if player.onground:
            player.dy = -20
            player.onground = False
            player.jump = True
    
    if key[pg.K_SPACE]:
        player.attack = True

    player.update(settings.HEIGHT - player.rect.height)
    screen.blit(background, (0, 0))
    screen.blit(player.image, player.rect)
    pg.display.update()
    clock.tick(60)

pg.quit()
