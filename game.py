#import standard library

#import external library
import pygame

#import local library
from characters import Guardian, Hero
from labyrinth import Labyrinth
from item import Item

#Initialization of the pygame library
pygame.init()

#variables
hero_image_path = "images/Hero.png"
hero_coordinates = (120, 360)
guardian_image_path = "images/Guardian.png"
guardian_coordinates = (280,40)
tile_image_path = "images/tile.png"
wall_image_path = "images/wall.png"

#Create window
size = (600, 600)
screen = pygame.display.set_mode(size)

#Create labyrinth
board_game = Labyrinth(tile_image_path, wall_image_path)
board_game.generate_labyrinth(screen)

#Create characters
MacGyver = Hero(hero_image_path)
MacGyver.position(screen, hero_coordinates, board_game.empty_places)

TheGuardian = Guardian(guardian_image_path)
TheGuardian.position(screen, guardian_coordinates, board_game.empty_places)

#Create items

pygame.display.flip()
#While :

input()