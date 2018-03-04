"""
Main script of the game. Click on it to start the game.

Tha MacGyver labyrinth game. MacGyver wants to escape from the labyrinth. But he needs to put to sleep the guardian.
For this purpose, he has to catch 3 items : a needle, a plastic tube and some ether.
"""

#import standard library
from time import sleep

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

#Initialize and play the song
pygame.mixer.music.load(music_path)
pygame.mixer.music.play()

#Create window
screen = pygame.display.set_mode(screen_size)

#Create labyrinth
board_game = Labyrinth(tile_image_path, wall_image_path, model_path)
board_game.initialize_labyrinth(screen)

#Create characters
macgyver = Hero(hero_image_path, macgyver_coordinates)
the_guardian = Guardian(guardian_image_path, the_guardian_coordinates)

#Create items
needle = Item(needle_image_path, board_game)
plastic_tube = Item(plastic_tube_image_path, board_game)
ether = Item(ether_image_path, board_game)

#The game loop
while active:

	#If the music stops, it starts again
	if pygame.mixer.music.get_busy() == False:
		pygame.mixer.music.play()

	#Display the game
	board_game.display_labyrinth(screen)
	macgyver.position(screen)
	the_guardian.position(screen)
	for item in Item.LIST_ITEMS:
		item.position(screen)

	pygame.display.flip()

	#When MacGyver meets the guardian
	if macgyver.coordinates == fight_coordinates:
		if macgyver.bag == 3:
			macgyver.send_to_sleep(board_game, the_guardian, arrival_coordinates)
		else:
			the_guardian.kill_hero(macgyver, dead_path)
			screen.blit(macgyver.face, macgyver.coordinates)
			active = False

	#If MacGyver reaches the arrival
	if macgyver.coordinates == arrival_coordinates:
		macgyver.win = True
		active = False
	
	#Event management
	for event in pygame.event.get():
		if event.type == QUIT:
			active = False
		if event.type == KEYDOWN:
			x, y = macgyver.move(event)

			#Empty place without a wall, a character or an item
			if (x,y) in board_game.empty_places:
				board_game.empty_places.remove((x,y))
				modif = True

			#Place where there is an item
			elif (x,y) in [item.coordinates for item in Item.LIST_ITEMS]:
				macgyver.bag += 1
				Item.LIST_ITEMS = [item for item in Item.LIST_ITEMS if item.coordinates != (x,y)]
				modif = True

			#Place where there is an obstacle
			else:
				modif = False

			#Move
			if modif == True:
				board_game.empty_places.append(macgyver.coordinates)
				macgyver.coordinates = (x,y)

#End of the game
if macgyver.win == True:
	path = you_win
else:
	path = game_over

#Display the right panel
panel = pygame.image.load(path).convert()
screen.blit(panel, (100,200))
pygame.display.flip()

#Wait 3 seconds
sleep(3)

#Stop the song
pygame.mixer.music.stop()