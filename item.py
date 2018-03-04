"""
Script that creates all the items of the game. There are derived from Item.
"""

#import standard library
import random

#import external library
import pygame

#Initialization of the pygame library
pygame.init()

class Item:
	"""Class from which my items are derived"""


	LIST_ITEMS = []

	def __init__(self, image_path, board_game):
		"""My constructor"""

		self.image = pygame.image.load(image_path).convert_alpha()
		self.coordinates = (0,0)

		self.generate_coordinates(board_game)
		Item.LIST_ITEMS.append(self)

	def generate_coordinates(self, board_game):
		"""Function that creates the coordinates for an item"""

		self.coordinates = random.choice(board_game.empty_places)
		board_game.empty_places.remove(self.coordinates)

	def position(self, screen):
		"""Function that positions the item"""

		screen.blit(self.image, self.coordinates)