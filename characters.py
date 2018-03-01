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

	def position(self, screen, empty_places):
		"""Function that positions the character"""

		try:
			empty_places.remove(self.coordinates)
		except ValueError:
			print("""Le personnage ne peut pas se trouver sur un mur.""")
		else:
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

	def move(self, event, screen):
		"""Function that allows the movement"""

		x, y = self.coordinates
		if event.key == K_UP:
			self.coordinates = (x,y-40)
		elif event.key == K_DOWN:
			self.coordinates = (x,y+40)
		elif event.key == K_RIGHT:
			self.coordinates = (x+40,y)
		elif event.key == K_LEFT:
			self.coordinates = (x-40,y)
		else:
			pass
		screen.blit(self.face, self.coordinates)

		#Take item