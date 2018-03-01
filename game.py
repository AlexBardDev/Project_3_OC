"""
Main script of the game. Click on it to start the game.
"""

#Author : Alexandre Bardiaux

#import standard library
import sys

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
board_game = Labyrinth(tile_image_path, wall_image_path)
board_game.initialize_labyrinth(screen)

#Create characters
MacGyver = Hero(hero_image_path, MacGyver_coordinates)
TheGuardian = Guardian(guardian_image_path, TheGuardian_coordinates)

#Create items
needle = Item(needle_image_path, board_game)
board_game.empty_places.remove(needle.coordinates)
list_items.append(needle)

plastic_tube = Item(plastic_tube_image_path, board_game)
board_game.empty_places.remove(plastic_tube.coordinates)
list_items.append(plastic_tube)

ether = Item(ether_image_path, board_game)
board_game.empty_places.remove(ether.coordinates)
list_items.append(ether)

pygame.display.flip()

while active:
	board_game.generate_labyrinth(screen)
	MacGyver.position(screen)
	TheGuardian.position(screen)
	for item in list_items:
		item.position(screen)

	for event in pygame.event.get():
		if event.type == QUIT:
			active = False
		if event.type == KEYDOWN:
			list_items = MacGyver.move(event, screen, board_game, list_items)

	pygame.display.flip()

sys.exit()