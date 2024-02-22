import os
import re
import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, file):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = 0
        self.dy = 0
        self.onground = False
        self.move = False
        self.frame = 0
        self.left = False
        self.right = True
        self.jump = False
        self.attack = False
        self.running = sorted(os.listdir('data/player/running/right'), key=lambda x: int(re.search(r'\d+', x).group()))
        self.holding = sorted(os.listdir('data/player/holding/right'), key=lambda x: int(re.search(r'\d+', x).group()))
        self.jumping = sorted(os.listdir('data/player/jumping/right'), key=lambda x: int(re.search(r'\d+', x).group()))
        self.attacking = sorted(os.listdir('data/player/attacking/right'), key=lambda x: int(re.search(r'\d+', x).group()))

    def update(self, tilemap):
        self.rect.x += self.dx
        self.check_collision_x(tilemap)
        
        if not self.onground:
            self.dy += 1.5

        self.rect.y += self.dy
        self.onground = False

        self.check_collision_y(tilemap)

        if self.right:
            file = 'right/'
        if self.left:
            file = 'left/'
        else:
            file = 'right/'

        if self.attack:
            self.frame += 0.2
            if self.frame >= len(self.attacking):
                self.attack = False
                self.frame = 0
            else:
                self.image = pg.image.load('data/player/attacking/' + file + self.attacking[int(self.frame)]).convert_alpha()
        elif not self.jump:
            if self.move:
                self.frame += 0.2
                if self.frame > 10:
                    self.frame -= 10

                self.image = pg.image.load('data/player/running/' + file + self.running[int(self.frame)]).convert_alpha()
            else:
                self.frame += 0.2
                if self.frame >= len(self.holding):
                    self.frame = 0

                self.image = pg.image.load('data/player/holding/' + file + self.holding[int(self.frame)]).convert_alpha()
        else:
            self.frame += 0.2
            if self.frame >= len(self.jumping):
                self.frame = 0

            self.image = pg.image.load('data/player/jumping/' + file + self.jumping[int(self.frame)]).convert_alpha()

        self.dx = 0

    def check_collision_x(self, tilemap):
        for tile in tilemap.tile_list:
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.rect.width, self.rect.height):
                if self.dx > 0:
                    self.rect.x = tile[1].x - self.rect.width
                elif self.dx < 0:
                    self.rect.x = tile[1].x + tile[1].width
                self.dx = 0

    def check_collision_y(self, tilemap):
        for tile in tilemap.tile_list:
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.rect.width, self.rect.height):
                if self.dy > 0:
                    self.rect.y = tile[1].y - self.rect.height
                    self.onground = True
                    self.dy = 0
                    self.jump = False
                elif self.dy < 0:
                    self.rect.y = tile[1].y + tile[1].height
                    self.dy = 0
