import pygame as pg
import settings
from player_folder.player import Player
from game_map_folder.game_map import game_map_data
from game_map_folder.mapping import World
from camera_folder.camera import Camera

pg.init()

screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
pg.display.set_caption("Platformer")

background = pg.image.load("data/background/backgroung.png").convert()
background = pg.transform.scale(background, (settings.WIDTH, settings.HEIGHT))

pg.mixer.music.load("data/audio/song_forest.mp3")
pg.mixer.music.play(-1)

dirt_image = pg.image.load("data/textures/Tile.png").convert_alpha()
clock = pg.time.Clock()

                  
player = Player(50, settings.HEIGHT - 100, "data/textures/Tile.png")
world = World(game_map_data)
camera = Camera(settings.WIDTH, settings.HEIGHT)

running = True

while running:

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

    player.update(world) #settings.HEIGHT - player.rect.height

    camera.set_target(player)
    camera.update(player)

    screen.blit(background, (0, 0)) # отрисовка заднего фона
    world.draw()
    screen.blit(player.image, camera.apply(player)) #screen.blit(player.image, player.rect) # отрисовка персонажа

    pg.display.update()
    clock.tick(60)

pg.quit()
