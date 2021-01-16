import pygame
from constants import *
from tile import Tile


class Map:

	def __init__(self, array, screen):

		self.array = array

		self.width = len(self.array[0]) # pega a largura da área do mapa
		self.height = len(self.array) # pega a altura da área do mapa

		self.tilesWall = pygame.sprite.Group()


		y = 0
		for _list in self.array:
			x = 0
			for item in _list:
				if item == 1:
					tile = Tile(TILESIZE*x, TILESIZE*y, TILESIZE, TILESIZE, YELLOW)
					self.tilesWall.add(tile)

				if item == 2:
					tile = Tile(TILESIZE*x, TILESIZE*y, TILESIZE, TILESIZE, GREEN)
					self.tilesWall.add(tile)

				x+=1
			y+=1

		print(self.tilesWall)



	def update(self, screen, player):

		self.tilesWall.draw(screen)

		hit = pygame.sprite.spritecollide(player, self.tilesWall, False)
		
		for item in hit:
			#####################################
			# verificação de colisão feita com sucesso
			if player.rect.y < item.rect.height:
				player.rect.top = item.rect.bottom

			if player.rect.x < item.rect.width:
				player.rect.left = item.rect.right


		





