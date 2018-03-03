"""
Script that creates the board game. It generates the labyrinth.
"""

#import standard library

#import external library
import pygame

#import local library
from constants import *

#Initialization of the pygame library
pygame.init()

class Labyrinth:
	"""Class from which my labyrinth is derived"""


	def __init__(self, tile_image_path, wall_image_path, model_path):
		"""My constructor"""

		self.tile = tile_image_path
		self.wall = wall_image_path
		self.model = model_path
		self.empty_places = []

	def initialize_labyrinth(self, screen):
		"""Function that initialize the labyrinth"""

		with open(self.model, "r") as data :
			model = data.read()

		j = 0
		for line in model.split("\n"):
			i = 0
			for letter in line:
				if letter == "O":
					image_path = self.wall
				else:
					image_path = self.tile
					self.empty_places.append((i,j))
				square = pygame.image.load(image_path).convert()
				screen.blit(square, (i,j))
				i += 40
			j += 40

		self.empty_places.remove(coord_1)
		self.empty_places.remove(coord_2)
		self.empty_places.remove(MacGyver_coordinates)
		self.empty_places.remove(TheGuardian_coordinates)

	def generate_labyrinth(self, screen):
		"""Function that creates the labyrinth"""

		with open(self.model, "r") as data :
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