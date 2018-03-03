"""
Script that contains the classes from which all the characters are derived.
"""

#import standard library

#import external library
import pygame
from pygame.locals import *

#import local library

#Initialization of the pygame library
pygame.init()


class Characters:
	"""Class from which my characters are derived"""


	def __init__(self, image_path, coordinates):
		"""My constructor"""

		self.face = pygame.image.load(image_path).convert_alpha()
		self.coordinates = coordinates

	def position(self, screen):
		"""Function that positions the character"""

		screen.blit(self.face, self.coordinates)


class Guardian(Characters):
	"""Class from which my guardian is derived"""


	def __init__(self, image_path, coordinates):
		"""My constructor"""

		Characters.__init__(self, image_path, coordinates)

	#Kill hero
	

class Hero(Characters):
	"""Class from which my hero is derived"""


	def __init__(self, image_path, coordinates):
		"""My constructor"""

		Characters.__init__(self, image_path, coordinates)
		self.bag = 0

	def move(self, event, screen, board_game, Item):
		"""Function that allows the movement"""

		x, y = self.coordinates
		if event.key == K_UP:
			y -= 40
		elif event.key == K_DOWN:
			y += 40
		elif event.key == K_RIGHT:
			x += 40
		elif event.key == K_LEFT:
			x -= 40
		else:
			pass

		if (x,y) in board_game.empty_places:
			board_game.empty_places.remove((x,y))
			modif = True
		elif (x,y) in [item.coordinates for item in Item.LIST_ITEMS]:
			self.bag += 1
			Item.LIST_ITEMS = [item for item in Item.LIST_ITEMS if item.coordinates != (x,y)]
			modif = True
		else:
			modif = False

		if modif == True:
			board_game.empty_places.append(self.coordinates)
			self.coordinates = (x,y)