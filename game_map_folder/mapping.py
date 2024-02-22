import pygame
import settings

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

class World():
	def __init__(self, data):
		self.tile_list = []

		#load images
		dirt_img = pygame.image.load('data/textures/Tile.png')
		dirt2_img = pygame.image.load('data/textures/Tile_2.png')

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 0:
					img = pygame.transform.scale(dirt_img, (settings.TILE_SIZE, settings.TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * settings.TILE_SIZE
					img_rect.y = row_count * settings.TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(dirt2_img, (settings.TILE_SIZE, settings.TILE_SIZE))
					img_rect = img.get_rect()
					img_rect.x = col_count * settings.TILE_SIZE
					img_rect.y = row_count * settings.TILE_SIZE
					tile = (img, img_rect)
					self.tile_list.append(tile)					
				col_count += 1
			row_count += 1


	def draw(self, camera_x, camera_y):
		for tile in self.tile_list:
			tile_img, tile_rect = tile
			screen.blit(tile_img, (tile_rect.x - camera_x, tile_rect.y - camera_y))		
	# def draw(self):
	# 	for tile in self.tile_list:
	# 		screen.blit(tile[0], tile[1])
