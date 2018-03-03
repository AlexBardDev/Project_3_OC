"""
Main script of the game. Click on it to start the game.

Tha MacGyver labyrinth game. MacGyver wants to escape from the labyrinth. But he needs to put to sleep the guardian.
For this purpose, he has to catch 3 items : a needle, a plastic_tube and some ether.
"""

#import standard library

#import external library
import pygame
from pygame.locals import *

#import local library
from constants import *
from labyrinth import Labyrinth
from characters import Guardian, Hero
from item import Item

#Initialization of the pygame library
pygame.init()

#Create window
screen = pygame.display.set_mode(screen_size)

#Create labyrinth
board_game = Labyrinth(tile_image_path, wall_image_path, model_path)
board_game.initialize_labyrinth(screen)

#Create characters
MacGyver = Hero(hero_image_path, MacGyver_coordinates)
TheGuardian = Guardian(guardian_image_path, TheGuardian_coordinates)

#Create items
needle = Item(needle_image_path, board_game)
plastic_tube = Item(plastic_tube_image_path, board_game)
ether = Item(ether_image_path, board_game)

while active:

	board_game.display_labyrinth(screen)
	MacGyver.position(screen)
	TheGuardian.position(screen)
	for item in Item.LIST_ITEMS:
		item.position(screen)

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == QUIT:
			active = False
		if event.type == KEYDOWN:
			MacGyver.move(event, screen, board_game, Item)