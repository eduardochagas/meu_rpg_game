import pygame
from constants import *
from tile import Tile
from camera import Camera
from player import Player


class PrincipalMap:

	def __init__(self, array_layers_map, screen):


		#####################################################
		# array que contém todas as layers do arquivo: layersMap1.py
		self.array_layers_map = array_layers_map

		#################################################################
		# self.tilewidth pega a largura da primeira layer do arquivo: layersMap1.py
		#  OBS: todas as layers tem o mesmo tamanho de largura e altura
		#  OBS2: todas as layers DEVEM TER O MESMO TAMANHO de largura e altura para funcionar corretamente
		self.tilewidth = len(self.array_layers_map[0][0]) # pega a largura da área do mapa
		############################################################
		# self.tileheight pega a largura da primeira layer do arquivo: layersMap1.py
		#  OBS: todas as layers tem o mesmo tamanho de largura e altura
		#  OBS2: todas as layers DEVEM TER O MESMO TAMANHO de largura e altura para funcionar corretamente
		self.tileheight = len(array_layers_map[0])# pega a altura da área do mapa 

		############################################################
		# self.width obtem o valor da multiplicação do comprimento
		# do primeiro array de self.array_layers_map com TILESIZE
		self.width = self.tilewidth * TILESIZE
		############################################################
		# self.height obtem o valor da multiplicação do comprimento
		# do primeiro array de self.array_layers_map com TILESIZE
		self.height = self.tileheight * TILESIZE

		########################################################3
		# o valor de self.width e self.height representa o valor
		# da LARGURA e da ALTURA da primeira layer em layersMap1.py
		self.camera = Camera(screen, self.width, self.height)


		self.all_tiles = pygame.sprite.Group() 

		self.tilesFloor = pygame.sprite.Group()

		self.tilesWall = pygame.sprite.Group()

		self.tilesVase = pygame.sprite.Group() # grupo de vasos de itens da tela (somente para teste)

		# self.tilesLife = pygame.sprite.Group() # grupo de itens de coração para sangue (somente para teste)

		self.groupPlayers = pygame.sprite.Group()




		self.drawLayer(self.array_layers_map[0])
		self.drawLayer(self.array_layers_map[1])
		self.drawLayer(self.array_layers_map[2])

		
		self.all_tiles.add(self.tilesFloor)
		self.all_tiles.add(self.tilesWall)
		self.all_tiles.add(self.tilesVase)
		# self.all_tiles.add(self.tilesLife)

		self.all_tiles.add(self.groupPlayers)





	def update(self, screen):
		
		self.player1.update(self.tilesWall, self.tilesVase)


		self.camera.update(self.player1)


		for sprite in self.all_tiles:
			screen.blit(sprite.image, self.camera.apply(sprite))



	def drawLayer(self, array_layers_map):

		y = 0
		for _list in array_layers_map:
			x = 0
			for item in _list:
				if item == 1:
					tile = Tile(TILESIZE*x, TILESIZE*y, TILESIZE, TILESIZE, YELLOW)
					self.tilesFloor.add(tile)

				if item == 2:
					tile = Tile(TILESIZE*x, TILESIZE*y, TILESIZE, TILESIZE, GREY)
					self.tilesWall.add(tile)

				if item == 3:
					tile = Tile(TILESIZE*x, TILESIZE*y, TILESIZE, TILESIZE, BROWN)
					self.tilesVase.add(tile)

				# if item == 4:
				# 	tile = Tile(TILESIZE*x, TILESIZE*y, TILESIZE, TILESIZE, REDLIGHT)
				# 	self.tilesLife.add(tile)

				if item == 'P':
					self.player1 = Player(TILESIZE*x, TILESIZE*y, TILESIZE, TILESIZE, 5)
					self.groupPlayers.add(self.player1)


				x+=1
			y+=1