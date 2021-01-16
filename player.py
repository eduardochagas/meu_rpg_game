import pygame
from constants import *


class Player(pygame.sprite.Sprite):

	def __init__(self, x, y, width, height, velocity):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width, height))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.velocity = velocity
		self.velx = 0
		self.vely = 0


		
	def update(self):

		self.controls()

	def controls(self):

		self.velx = 0
		self.vely = 0

		key = pygame.key.get_pressed()

		if key[pygame.K_a]:
			self.velx -= self.velocity
		if key[pygame.K_d]:
			self.velx += self.velocity
		if key[pygame.K_w]:
			self.vely -= self.velocity
		if key[pygame.K_s]:
			self.vely += self.velocity

		if self.velx != 0 and self.vely != 0:
			self.velx /= 1.414
			self.vely /= 1.414

		self.rect.x += self.velx
		self.rect.y += self.vely
			

