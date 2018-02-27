#import standard library

#import external library
import pygame

#import local library


class Characters:
	"""Class from which my characters are derived"""


	def __init__(self, image_path):
		"""My constructor"""

		self.face = pygame.image.load(image_path)


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