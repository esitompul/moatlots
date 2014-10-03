"""
Animation Windows for The Game
"""

import pygame, sys
from pygame.locals import *
from Asset import *

pygame.init()

#Frame per seconds settings
max_fps = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Testing an Animation')

MONOKAI	= (41,	36,	41	)
gengarImage = pygame.image.load('asset/Player/p1_stand.png')

gengar_x = 0
gengar_y = 440
direction = 'right'
pygame.key.set_repeat(50, 50)
dirt_height = 35

while  True:
	#keypress

	DISPLAYSURF.fill(MONOKAI)

	"""if direction == 'right' :
		gengar_x += 1
		if gengar_x == 250:
			direction = 'down'
	elif direction == 'down':
	    gengar_y += 10
	    if gengar_y== 250:
	        direction = 'left'
	elif direction == 'left':
	    gengar_x -= 10
	    if gengar_x == 10:
	        direction = 'up'
	elif direction == 'up':
	    gengar_y -= 10
	    if gengar_y == 10:
	        direction = 'right' """

	DISPLAYSURF.blit(dirtImage, (0, 530))
	
	
	DISPLAYSURF.blit(gengarImage, (gengar_x, gengar_y))


	for event in pygame.event.get():

		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif (pygame.key.get_pressed()[pygame.K_UP]):
			gengar_y -= 10
		elif (pygame.key.get_pressed()[pygame.K_DOWN]):
			gengar_y += 10
		elif (pygame.key.get_pressed()[pygame.K_RIGHT]):
			gengar_x += 10
		elif (pygame.key.get_pressed()[pygame.K_LEFT]):
			gengar_x -= 10	
	pygame.display.update()