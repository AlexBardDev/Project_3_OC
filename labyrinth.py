"""
Script that creates the board game.

Labyrinth initializes and displays the board game.
"""

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

		#Some special places to remove
		self.empty_places.remove(arrival_coordinates)
		self.empty_places.remove(macgyver_coordinates)
		self.empty_places.remove(the_guardian_coordinates)

	def display_labyrinth(self, screen):
		"""Function that displays the labyrinth"""

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