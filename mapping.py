import pygame as pg


class Tilemap:
    def __init__(self, tile_size, map_data):
        self.tile_size = tile_size
        self.map_data = map_data
        self.tiles = []

        for row_index, row in enumerate(map_data):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    rect = pg.Rect(col_index * tile_size, row_index * tile_size, tile_size, tile_size)
                    self.tiles.append(rect)

    def draw(self, surface):
        for tile in self.tiles:
            pg.draw.rect(surface, (255, 255, 255), tile)
