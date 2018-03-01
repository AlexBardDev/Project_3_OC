#import standard library
import sys

#import external library
import pygame
from pygame.locals import *

#import local library
from characters import Guardian, Hero
from labyrinth import Labyrinth
from item import Item
from constants import *

#Initialization of the pygame library
pygame.init()

#Create window
screen = pygame.display.set_mode(screen_size)

#Create labyrinth
board_game = Labyrinth(tile_image_path, wall_image_path)
board_game.generate_labyrinth(screen)

#Create characters
MacGyver = Hero(hero_image_path)
MacGyver.position(screen, board_game.empty_places)

TheGuardian = Guardian(guardian_image_path)
TheGuardian.position(screen, board_game.empty_places)

#Remove 2 places that MacGyver can't reach because of the guardian
board_game.empty_places.remove((280,0))
board_game.empty_places.remove((320,40))

#Create items
needle = Item(needle_image_path, board_game.empty_places)
needle.position(screen)
board_game.empty_places.remove(needle.coordinates)

plastic_tube = Item(plastic_tube_image_path, board_game.empty_places)
plastic_tube.position(screen)
board_game.empty_places.remove(plastic_tube.coordinates)

ether = Item(ether_image_path, board_game.empty_places)
ether.position(screen)
board_game.empty_places.remove(ether.coordinates)

pygame.display.flip()

while active:
	board_game.generate_labyrinth(screen)
	MacGyver.position(screen, board_game.empty_places)
	TheGuardian.position(screen, board_game.empty_places)
	needle.position(screen)
	plastic_tube.position(screen)
	ether.position(screen)

	for event in pygame.event.get():
		if event.type == QUIT:
			active = False
		if event.type == KEYDOWN:
			MacGyver.move(event, screen)

	pygame.display.flip()

sys.exit()