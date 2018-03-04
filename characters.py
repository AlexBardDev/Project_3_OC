"""
Script that contains the classes from which all the characters are derived.

There are 3 classes. 'Characters' is the base class of all the characters. 
'Guardian' and 'Hero' are derived classes from 'Characters'.
"""

#import external library
import pygame
from pygame.locals import *

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
	"""Class from which my guardian is derived. It inherits from Characters."""


	def __init__(self, image_path, coordinates):
		"""My constructor. It calls the constructor of Characters"""

		Characters.__init__(self, image_path, coordinates)

	def kill_hero(self, macgyver, dead_path):
		"""Function that kills MacGyver if the guardian is not asleep"""

		macgyver.face = pygame.image.load(dead_path).convert_alpha()

class Hero(Characters):
	"""Class from which my hero is derived. It inherits from Characters."""


	def __init__(self, image_path, coordinates):
		"""My constructor. It calls the constructor of Characters"""

		Characters.__init__(self, image_path, coordinates)
		self.bag = 0
		self.win = False

	def move(self, event):
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

		return x, y

	def send_to_sleep(self, board_game, the_guardian, arrival_coordinates):
		"""Function that sends the guardian to sleep"""

		board_game.empty_places.append(the_guardian.coordinates)
		board_game.empty_places.append(arrival_coordinates)
