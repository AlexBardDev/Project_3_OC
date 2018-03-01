#import standard library
import random

#import external library
import pygame

#import local library

#Initialization of the pygame library
pygame.init()

class Item:
	"""Class from which my items are derived"""


	def __init__(self, image_path, empty_places):
		"""My constructor"""

		self.image = pygame.image.load(image_path).convert_alpha()
		self.coordinates = random.choice(empty_places)

	def position(self, screen):
		"""Function that positions the item"""

		screen.blit(self.image, self.coordinates)