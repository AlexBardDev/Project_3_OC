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

	if MacGyver.coordinates == fight_coordinates:
		if MacGyver.bag == 3:
			MacGyver.send_to_sleep(board_game, TheGuardian, arrival_coordinates)
		else:
			TheGuardian.kill_hero(MacGyver)
			active = False

	if MacGyver.coordinates == arrival_coordinates:
		active = False
	
	for event in pygame.event.get():
		if event.type == QUIT:
			active = False
		if event.type == KEYDOWN:
			x, y = MacGyver.move(event)

			if (x,y) in board_game.empty_places:
				board_game.empty_places.remove((x,y))
				modif = True
			elif (x,y) in [item.coordinates for item in Item.LIST_ITEMS]:
				MacGyver.bag += 1
				Item.LIST_ITEMS = [item for item in Item.LIST_ITEMS if item.coordinates != (x,y)]
				modif = True
			else:
				modif = False

			if modif == True:
				board_game.empty_places.append(MacGyver.coordinates)
				MacGyver.coordinates = (x,y)