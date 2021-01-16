import pygame
from constants import *
from player import Player
from map import Map



class Game:

	def __init__(self):
		
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()

		self.all_sprites = pygame.sprite.Group()

		self.player1 = Player(TILESIZE * 5, TILESIZE * 5, TILESIZE, TILESIZE, 5)
		self.all_sprites.add(self.player1)

		self.map = Map(r1, self.screen)




		self.running = True
		self.loop()

	def loop(self):

		while self.running:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

			self.screen.fill(BLACK)

			self.all_sprites.draw(self.screen)

			self.all_sprites.update()



			self.map.update(self.screen, self.player1)





			pygame.display.update()
			self.clock.tick(FPS)



if __name__ == '__main__':
	Game()