"""
Script that creates all the items of the game.
"""

#Author : Alexandre Bardiaux

#import standard library
import random

#import external library
import pygame

#import local library

#Initialization of the pygame library
pygame.init()

class Item:
	"""Class from which my items are derived"""


	LIST_ITEMS = []

	def __init__(self, image_path, board_game):
		"""My constructor"""

		self.image = pygame.image.load(image_path).convert_alpha()
		self.coordinates = random.choice(board_game.empty_places)
		Item.LIST_ITEMS.append(self)

	def position(self, screen):
		"""Function that positions the item"""

		screen.blit(self.image, self.coordinates)