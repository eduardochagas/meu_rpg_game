import pygame
from constants import *


class Camera:

	def __init__(self, screen, widthMap, heightMap):
		self.width = widthMap
		self.height = heightMap
		self.cam = pygame.Rect(0,0,self.width, self.height)

		self.screen = screen



	def apply(self, target):

		return target.rect.move(self.cam.topleft)


	def update(self, player):

		
		x = -player.rect.x + int(WIDTH / 2) # 400px
		y = -player.rect.y + int(HEIGHT / 2) # 300px

		x = min(0, x)
		y = min(0, y)

		
		x = max(-(self.width - WIDTH), x)
		y = max(-(self.height - HEIGHT), y)


		#pygame.draw.rect(self.screen, (RED), (x, y, self.width, self.height), 5)

		self.cam = pygame.Rect(x, y, self.width, self.height)


	
