"""
Script that contains the classes from which all the characters are derived.
"""

#Author : Alexandre Bardiaux

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

	def move(self, event, screen, board_game):
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
			board_game.empty_places.append(self.coordinates)
			board_game.empty_places.remove((x,y))
			self.coordinates = (x,y)
		else:
			pass

	#Take item