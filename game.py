#import standard library

#import external library
import pygame

#import local library
from characters import Guardian, Hero
from labyrinth import Labyrinth
from item import Item

hero_image_path = "images/Hero.png"

#Generer le laby
#Generer les perso
#Placer les objets et les perso

size = 600, 600
screen = pygame.display.set_mode(size)

MacGyver = Hero(hero_image_path)
screen.blit(MacGyver.face, (200,300))

pygame.display.flip()
#While :