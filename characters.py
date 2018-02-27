#import standard library

#import external library
import pygame

#import local library

#Initialization of the pygame library
pygame.init()


class Characters:
	"""Class from which my characters are derived"""


	def __init__(self, image_path):
		"""My constructor"""

		self.face = pygame.image.load(image_path).convert_alpha()

	def position(self, screen, coordinates, empty_places):
		"""Function that positions the character"""

		try:
			empty_places.remove(coordinates)
		except ValueError:
			print("""Le personnage ne peut pas se trouver sur un mur.""")
		else:
			screen.blit(self.face, coordinates)


class Guardian(Characters):
	"""Class from which my guardian is derived"""


	def __init__(self, image_path):
		"""My constructor"""

		Characters.__init__(self, image_path)

	#Kill hero
	

class Hero(Characters):
	"""Class from which my hero is derived"""


	def __init__(self, image_path):
		"""My constructor"""

		Characters.__init__(self, image_path)

	#Move
	#Take item