#import standard library

#import external library
import pygame

#import local library

#Initialization of the pygame library
pygame.init()

class Labyrinth:
	"""Class from which my labyrinth is derived"""


	def __init__(self, tile_image_path, wall_image_path):
		"""My constructor"""

		self.tile = tile_image_path
		self.wall = wall_image_path

	def generate_labyrinth(self, screen):
		"""function that creates the labyrinth"""

		with open("lab.txt", "r") as data :
			model = data.read()

		j = 0
		for line in model.split("\n"):
			i = 0
			for letter in line:
				if letter == "O":
					image_path = self.wall
				else:
					image_path = self.tile
				square = pygame.image.load(image_path).convert()
				screen.blit(square, (i,j))
				i += 40
			j += 40
