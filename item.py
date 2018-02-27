#import standard library
import random

#import external library
import pygame

#import local library

#Initialization of the pygame library
pygame.init()

class Item:
	"""Class from which my items are derived"""


	def __init__(self, image_path):
		"""My constructor"""

		self.image = pygame.image.load(image_path).convert_alpha()

	def position(self, screen, empty_places):
		"""Function that positions the item"""

		coordinates = random.choice(empty_places)
		empty_places.remove(coordinates)
		screen.blit(self.image, coordinates)