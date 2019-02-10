# TODO:
# key held down movement
# have random missles/gun_fire flow down the screen
# have contact with jet = death / game start over
# 


import pygame
import sys
import random
import os



def main():
	pygame.init()
	W = 900
	H = 600
	size = (W, H)
	color = (0, 255, 0)
	display = pygame.display.set_mode(size)
	bg = pygame.image.load("background.jpg").convert()
	bg = pygame.transform.scale(bg, (W, H))
	pygame.display.set_caption('Aviators')
	clock = pygame.time.Clock()

	running = True
	while running:
		clock.tick(60)
		display.blit(bg, (0,0))
		pygame.draw.polygon(display, color, [[450, 540], [435, 575], [465, 575]], 2)

		for event in pygame.event.get():
#		keys = pygame.key.get_pressed()
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					img_x -=20
				if event.key == pygame.K_RIGHT:
					img_x +=20
		
			pygame.display.flip()
			pygame.display.update()

pygame.quit()


if __name__ == "__main__":
	main()


