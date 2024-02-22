import pygame as pg
import settings
from player_folder.player import Player
from game_map_folder.game_map import level
from game_map_folder.mapping import World

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
camera_x = 0
camera_y = 0
world = World(level)


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


    player.update(world, camera_x, camera_y)

    if player.rect.right > settings.WIDTH / 2:
        camera_x += player.dx
        # Предотвращение выхода за пределы карты вправо
        if camera_x > (len(level[0]) * settings.TILE_SIZE) - settings.WIDTH:
            camera_x = (len(level[0]) * settings.TILE_SIZE) - settings.WIDTH
    camera_x = player.rect.x - settings.WIDTH // 2
    camera_y = player.rect.y - settings.HEIGHT // 2
    # Ограничение координат камеры, чтобы не выходить за пределы карты
    camera_x = max(0, min(camera_x, (len(level[0]) - settings.WIDTH // settings.TILE_SIZE) * settings.TILE_SIZE))
    camera_y = max(0, min(camera_y, (len(level) - settings.HEIGHT // settings.TILE_SIZE) * settings.TILE_SIZE))

     # отрисовка заднего фона
    screen.blit(background, (0, 0))
    # отрисовка тайлов
    world.draw(camera_x, camera_y)
     # отрисовка персонажа
    screen.blit(player.image, (player.rect.x - camera_x, player.rect.y - camera_y))

    pg.display.update()
    clock.tick(60)

pg.quit()
