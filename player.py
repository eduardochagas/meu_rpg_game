import pygame
from constants import *


class Player(pygame.sprite.Sprite):

	def __init__(self, x, y, width, height, velocity):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width, height))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.position = pygame.math.Vector2(x, y)
		self.rect.x = self.position.x
		self.rect.y = self.position.y
		self.velocity = velocity
		self.velx = 0
		self.vely = 0


		
	def update(self, *Groups_tile):

		self.controls()
		
		vec = pygame.math.Vector2(self.velx, self.vely)

		if (vec.x != 0 or vec.y != 0) or (vec.x != 0 and vec.y != 0):
			vec = vec.normalize()
			# print(vec)

		# escalando o vetor normalizado
		vec.x *= self.velocity
		vec.y *= self.velocity

		# atribui o x e y do vetor de velocidade
		self.position.x += vec.x
		self.position.y += vec.y

		# atribui o valor x do vetor position ao x do rect do player
		self.rect.x = self.position.x


		groupsTile = [*Groups_tile] # desempacota cada grupo passado, onde cada grupo é um item do array

		for group in groupsTile:
			self.collisionPlayerWithGroup('x', group, False)

		self.rect.y = self.position.y


		for group in groupsTile:
			self.collisionPlayerWithGroup('y', group, False)


		self.velx = 0
		self.vely = 0



	def controls(self):

		key = pygame.key.get_pressed()

		if key[pygame.K_a]:
			self.velx = -1

		if key[pygame.K_d]:
			self.velx = 1

		if key[pygame.K_w]:
			self.vely = -1

		if key[pygame.K_s]:
			self.vely = 1


	#############################################################
	# faz o teste de colisão com os grupos de tiles do(s) mapa(s)
	#
	def collisionPlayerWithGroup(self, axis, group_tile, boolean):


		if axis == 'x':

			hit = pygame.sprite.spritecollide(self, group_tile, boolean)

			if hit:
				if self.velx > 0:
					self.position.x = hit[0].rect.x - self.rect.width

				elif self.velx < 0:
					self.position.x = hit[0].rect.x + hit[0].rect.width

			self.rect.x = self.position.x


		if axis == 'y':

			hit = pygame.sprite.spritecollide(self, group_tile, False)

			if hit:
				if self.vely < 0:
					self.position.y = hit[0].rect.y + hit[0].rect.height
				
				elif self.vely > 0:
					self.position.y = hit[0].rect.y - self.rect.height


			self.rect.y = self.position.y


