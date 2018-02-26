#import standard library

#import external library
import pygame

#import local library
from characters import Guardian, Hero
from labyrinth import Labyrinth

#Generer le laby
#Generer les perso
#Placer les objets et les perso

size = 600, 600
screen = pygame.display.set_mode(size)

hero = pygame.image.load("images/Hero.png")
screen.blit(hero, (200,300))

pygame.display.flip()
#While :