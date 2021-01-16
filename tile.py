import pygame



class Tile(pygame.sprite.Sprite):

	def __init__(self, x, y, width, height, color):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width, height))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y