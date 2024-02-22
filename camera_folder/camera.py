import pygame as pg
import settings

class Camera:
    def __init__(self, width, height, level_width, level_height):
        self.width = width
        self.height = height
        self.level_width = level_width * settings.TILE_SIZE
        self.level_height = level_height * settings.TILE_SIZE

        self.camera_x = 0
        self.camera_y = 0

    def update(self, target_rect):
        # Следование за игроком по оси X
        self.camera_x = target_rect.x - self.width // 2
        # Ограничение координат камеры, чтобы не выходить за пределы карты
        self.camera_x = max(0, min(self.camera_x, self.level_width - self.width))

        # Следование за игроком по оси Y
        self.camera_y = target_rect.y - self.height // 2
        # Ограничение координат камеры, чтобы не выходить за пределы карты
        self.camera_y = max(0, min(self.camera_y, self.level_height - self.height))

    def apply(self, entity_rect):
        # Перевод координат объекта из координат мира в координаты камеры
        return entity_rect.x - self.camera_x, entity_rect.y - self.camera_y
