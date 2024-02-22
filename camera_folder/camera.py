import pygame as pg
import settings
from game_map_folder.game_map import level


# class Camera:
#     def __init__(self, width, height):
#         self.camera = pg.Rect(0, 0, width, height)
#         self.width = width
#         self.height = height

#     def apply_rect(self, rect):
#         return rect.move(self.camera.topleft)
    
#     def apply(self, target):
#         return target.rect.move(self.camera.topleft)

#     def update(self, target):
#         x = -target.rect.x + int(settings.WIDTH / 2)
#         y = -target.rect.y + int(settings.HEIGHT / 2)
#         x = min(0, x)
#         y = min(0, y)
#         x = max(-(self.width - settings.WIDTH), x)
#         y = max(-(self.height - settings.HEIGHT), y)

#         self.camera = pg.Rect(x, y, self.width, self.height)
