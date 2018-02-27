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
guardian_image_path = "images/Guardian.png"
wall_image_path = "images/tiles.png"

#Generer fenêtre
size = (600, 600)
screen = pygame.display.set_mode(size)

#Generer le laby
board = Labyrinth(wall_image_path)
board.generate_labyrinth(screen)

#Generer les perso
MacGyver = Hero(hero_image_path)
screen.blit(MacGyver.face, (120,400))

TheGuardian = Guardian(guardian_image_path)
screen.blit(TheGuardian.face, (280,40))

#Placer les objets et les perso

pygame.display.flip()
#While :

input()