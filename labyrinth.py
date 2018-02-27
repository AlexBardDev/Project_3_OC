#import standard library

#import external library
import pygame

#import local library

#Initialization of the pygame library
pygame.init()

class Labyrinth:
	"""Class from which my labyrinth is derived"""


	def __init__(self, image_path):
		"""My constructor"""

		self.image = image_path

	def generate_labyrinth(self, screen):
		"""function that creates the labyrinth"""

		j = 0
		for y in range(15):
			i = 0
			for x in range(15):
				square = pygame.image.load(self.image).convert()
				screen.blit(square, (i,j))
				i += 40
			j += 40
