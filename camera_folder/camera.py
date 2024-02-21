import pygame as pg
import settings


class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #self.target = None
        self.camera = pg.Rect(0, 0, width, height)

    def set_target(self, target):
        self.target = target

    def apply(self, target): #entity
        return target.rect.move(self.camera.topleft) #return entity.rect.move(self.camera.topleft)

    def update(self, target):
        if self.target:
            x = -target.rect.x + settings.WIDTH / 2
            y = -target.rect.y + settings.HEIGHT / 2

            x = min(0, x)
            y = min(0, y)
            x = max(-(self.width - settings.WIDTH), x)
            y = max(-(self.height - settings.HEIGHT), y)

            self.camera = pg.Rect(x, y, self.width, self.height)
# class Camera:
#     def __init__(self, width, height):
#         self.camera = pg.Rect(0, 0, width, height)
#         self.width = width
#         self.height = height

#     def apply(self, target):
#         return target.rect.move(self.camera.topleft)

#     def update(self, target):
#         x = -target.rect.x + settings.WIDTH // 2
#         y = -target.rect.y + settings.HEIGHT // 2

#         # Limit scrolling to the boundaries of the map
#         x = min(0, x)  # left
#         y = min(0, y)  # top
#         x = max(-(self.width - settings.WIDTH), x)  # right
#         y = max(-(self.height - settings.HEIGHT), y)  # bottom

#         self.camera = pg.Rect(x, y, self.width, self.height)

