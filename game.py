import pygame
from constants import *
from layersMap1 import *
from layersMap2 import *
from player import Player
from map import Map
from camera import Camera



class Game:

	def __init__(self):
		
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()


		self.array_maps_game = []


		self.map = Map(layersMap1, self.screen)
		self.array_maps_game.append(self.map)

		# self.map2 = Map(layersMap2, self.screen)
		# self.array_maps_game.append(self.map2)


		self.num_map = 0

		self.running = True
		self.loop()

	def loop(self):

		while self.running:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

			self.screen.fill(BLACK)

			if self.num_map == 0:
				self.map.update(self.screen)
				# if self.player1.rect.left > WIDTH:
				# 	self.map2.update(self.screen, self.player1)

			# self.all_players.draw(self.screen)

			# self.all_players.update()




			pygame.display.update()
			self.clock.tick(FPS)



if __name__ == '__main__':
	Game()